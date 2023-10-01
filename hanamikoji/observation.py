from dataclasses import dataclass
from typing import List, Optional, Any

from .cards_set import CardsSet


@dataclass
class Observation:
    geishas: List[Optional[int]]
    geishas_cards: List[CardsSet]
    current_player: int
    cards: CardsSet
    deck: CardsSet
    hidden: CardsSet
    discarded: CardsSet
    actions: List[List[bool]]
    pending_action: Optional[Any]
