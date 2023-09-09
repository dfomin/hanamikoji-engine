import random
from dataclasses import dataclass
from typing import List, Optional, Any

# from action import Action
from cards_set import CardsSet
from observation import Observation

GEISHAS_COUNT = [2, 2, 2, 3, 3, 4, 5]
CARDS_COUNT = sum(GEISHAS_COUNT)
CARDS_INDEX_MAP = [i for i, j in enumerate(GEISHAS_COUNT) for _ in range(j)]


@dataclass
class Score:
    points: List[int]
    geishas: List[int]

    def winner(self) -> Optional[int]:
        if self.points[0] >= 11:
            return 0
        elif self.points[1] >= 11:
            return 1

        if self.geishas[0] >= 4:
            return 0
        elif self.geishas[1] >= 4:
            return 1

        return None


class State:
    geishas: List[Optional[int]]
    current_player: int
    cards: List[CardsSet]
    deck: CardsSet
    hidden: List[CardsSet]
    discarded: List[CardsSet]
    actions: List[List[bool]]
    pending_action: Optional[Any]

    @property
    def opponent(self):
        return 1 - self.current_player

    def __init__(self):
        self.geishas = [None] * len(GEISHAS_COUNT)
        self.current_player = random.randint(0, 1)

        cards_indices = [0] * len(GEISHAS_COUNT) + [1] * len(GEISHAS_COUNT) + [-1] * (CARDS_COUNT - 2 * len(GEISHAS_COUNT))
        random.shuffle(cards_indices)
        self.cards = [CardsSet(), CardsSet()]
        self.deck = CardsSet()
        for card_index, player_index in enumerate(cards_indices):
            if player_index != -1:
                self.cards[player_index].add_card(CARDS_INDEX_MAP[card_index])
            else:
                self.deck.add_card(CARDS_INDEX_MAP[card_index])

        self.hidden = [CardsSet(), CardsSet()]
        self.discarded = [CardsSet(), CardsSet()]
        self.actions = [[True] * 4, [True] * 4]
        self.pending_action = None

    def winner(self) -> Optional[int]:
        return self.score().winner()

    def is_finished(self) -> bool:
        return self.winner() is not None

    def score(self) -> Score:
        geishas_points = GEISHAS_COUNT
        score = Score([0, 0], [0, 0])
        for i in range(len(GEISHAS_COUNT)):
            for player_index in range(2):
                if self.geishas[player_index] == player_index:
                    score.points[player_index] += geishas_points[i]
                    score.geishas[player_index] += 1

        return score

    def observation(self) -> Observation:
        return Observation(
            self.geishas,
            self.current_player,
            self.cards[self.current_player],
            self.deck,
            self.hidden[self.current_player],
            self.discarded[self.current_player],
            self.actions,
            self.pending_action,
        )
