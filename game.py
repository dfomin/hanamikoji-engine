from typing import List

from action import Action, SecretAction, TradeOffAction, GiftAction, CompetitionAction, ChooseGiftAction, \
    ChooseCompetitionAction
from player import Player
from state import State


class Game:
    players: List[Player]
    state: State

    def __init__(self, players: List[Player]):
        self.players = players
        self.state = State()

    def __str__(self) -> str:
        return str(self.state)

    def is_finished(self) -> bool:
        return self.state.is_finished()

    def update(self):
        actions = self.get_available_actions()
        action_index = self.players[self.state.current_player].choose_action(self.state.observation(), actions)
        action = actions[action_index]
        action.apply(self.state)
        self.state.current_player = 1 - self.state.current_player

    def get_available_actions(self) -> List[Action]:
        actions = []
        player_cards = self.state.cards[self.state.current_player]
        if self.state.pending_action is None:
            available_actions = self.state.actions[self.state.current_player]
            if available_actions[0]:
                actions.extend([SecretAction(s) for s in player_cards.select(1)])
            if available_actions[1]:
                actions.extend([TradeOffAction(s) for s in player_cards.select(2)])
            if available_actions[2]:
                actions.extend([GiftAction(s) for s in player_cards.select(3)])
            if available_actions[3]:
                # TODO: optimization required
                for cards in player_cards.select(4):
                    pairs = set()
                    for pair in cards.select(2):
                        if pair in pairs:
                            continue
                        rest = cards.clone()
                        rest.remove(pair)
                        pairs.add(rest)
                        actions.append(CompetitionAction([pair, rest]))
        elif isinstance(self.state.pending_action, GiftAction):
            cards = self.state.pending_action.cards
            actions.extend([ChooseGiftAction(s, cards.clone().remove(s)) for s in cards.select(1)])
        elif isinstance(self.state.pending_action, CompetitionAction):
            actions.append(ChooseCompetitionAction(take_cards=self.state.pending_action.card_sets[0],
                                                   give_cards=self.state.pending_action.card_sets[1]))
            actions.append(ChooseCompetitionAction(take_cards=self.state.pending_action.card_sets[1],
                                                   give_cards=self.state.pending_action.card_sets[0]))

        return actions
