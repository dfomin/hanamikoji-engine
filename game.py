from typing import List

from action import Action
from player import Player
from state import State


class Game:
    players: List[Player]
    state: State

    def __init__(self, players: List[Player]):
        self.players = players
        self.state = State()

    def is_finished(self):
        self.state.is_finished()

    def update(self):
        actions = self.get_available_actions()
        self.players[self.state.current_player].choose_action(self.state.observation(), actions)

    def get_available_actions(self) -> List[Action]:
        return []
