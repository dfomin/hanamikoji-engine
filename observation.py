from dataclasses import dataclass
from typing import List, Optional, Any

# from action import Action
from cards_set import CardsSet


@dataclass
class Observation:
    geishas: List[Optional[int]]
    current_player: int
    cards: CardsSet
    deck: CardsSet
    hidden: CardsSet
    discarded: CardsSet
    actions: List[List[bool]]
    pending_action: Optional[Any]
