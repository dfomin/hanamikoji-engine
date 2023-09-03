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

    def apply(self, state: State):
        state.hidden[state.current_player] = self.cards


@dataclass
class TradeOffAction(Action):
    cards: CardsSet

    def apply(self, state: State):
        state.discarded[state.current_player] = self.cards


@dataclass
class GiftAction(Action):
    cards: CardsSet

    def apply(self, state: State):
        pass


@dataclass
class ChooseGiftAction(Action):
    take_cards: CardsSet
    give_cards: CardsSet

    def apply(self, state: State):
        state.cards[state.current_player].add(self.take_cards)
        state.cards[state.opponent].add(self.give_cards)


@dataclass
class CompetitionAction(Action):
    card_sets: List[CardsSet]

    def apply(self, state: State):
        pass


@dataclass
class ChooseCompetitionAction(Action):
    take_cards: CardsSet
    give_cards: CardsSet

    def apply(self, state: State):
        state.cards[state.current_player].add(self.take_cards)
        state.cards[state.opponent].add(self.give_cards)
