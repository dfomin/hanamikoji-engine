from dataclasses import dataclass
from typing import Protocol, List

from cards_set import CardsSet
from state import State


class Action(Protocol):
    def apply(self, state: State):
        pass


@dataclass
class SecretAction(Action):
    cards: CardsSet

    def __str__(self) -> str:
        return f"Secret({self.cards})"

    def apply(self, state: State):
        state.hidden[state.current_player] = self.cards


@dataclass
class TradeOffAction(Action):
    cards: CardsSet

    def __str__(self) -> str:
        return f"TradeOff({self.cards})"

    def apply(self, state: State):
        state.discarded[state.current_player] = self.cards


@dataclass
class GiftAction(Action):
    cards: CardsSet

    def __str__(self) -> str:
        return f"Gift({self.cards})"

    def apply(self, state: State):
        state.pending_action = self


@dataclass
class ChooseGiftAction(Action):
    take_cards: CardsSet
    give_cards: CardsSet

    def __str__(self) -> str:
        return f"ChooseGift({self.take_cards}, {self.give_cards})"

    def apply(self, state: State):
        state.geishas_cards[state.current_player].add(self.take_cards)
        state.geishas_cards[state.opponent].add(self.give_cards)
        state.pending_action = None


@dataclass
class CompetitionAction(Action):
    card_sets: List[CardsSet]

    def __init__(self, cards_set: List[CardsSet]):
        self.card_sets = cards_set

    def __str__(self) -> str:
        return f"Competition({self.card_sets[0]}, {self.card_sets[1]})"

    def apply(self, state: State):
        state.pending_action = self


@dataclass
class ChooseCompetitionAction(Action):
    take_cards: CardsSet
    give_cards: CardsSet

    def __str__(self) -> str:
        return f"ChooseCompetition({self.take_cards}, {self.give_cards})"

    def apply(self, state: State):
        state.geishas_cards[state.current_player].add(self.take_cards)
        state.geishas_cards[state.opponent].add(self.give_cards)
        state.pending_action = None
