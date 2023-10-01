from typing import List

from .action import Action, SecretAction, TradeOffAction, GiftAction, CompetitionAction, ChooseGiftAction, \
    ChooseCompetitionAction
from .player import Player
from .state import State


class Game:
    @staticmethod
    def apply_action(state: State, action: Action):
        real_action = state.pending_action is None
        action.apply(state)

        if real_action:
            state.current_player = 1 - state.current_player

        if state.is_round_finished():
            for i in range(2):
                state.geishas_cards[i].add(state.hidden[i])
            state.assign_geishas()

            if state.is_finished():
                return

            state.current_player = 1 - state.current_player

            if not state.is_finished():
                state.new_round()
        elif state.pending_action is None:
            state.cards[state.current_player].add_card(state.deck.pop())

    @staticmethod
    def get_available_actions(state: State) -> List[Action]:
        actions = []
        player_cards = state.cards[state.current_player]
        if state.pending_action is None:
            available_actions = state.actions[state.current_player]
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
        elif isinstance(state.pending_action, GiftAction):
            cards = state.pending_action.cards
            for card in cards.select(1):
                rest = cards.clone()
                rest.remove(card)
                actions.append(ChooseGiftAction(card, rest))
        elif isinstance(state.pending_action, CompetitionAction):
            actions.append(ChooseCompetitionAction(take_cards=state.pending_action.card_sets[0],
                                                   give_cards=state.pending_action.card_sets[1]))
            if state.pending_action.card_sets[0] != state.pending_action.card_sets[1]:
                actions.append(ChooseCompetitionAction(take_cards=state.pending_action.card_sets[1],
                                                       give_cards=state.pending_action.card_sets[0]))

        return actions
