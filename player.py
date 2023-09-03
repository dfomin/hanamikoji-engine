from typing import List, Protocol

from action import Action
from observation import Observation


class Player(Protocol):
    index: int

    def choose_action(self, observation: Observation, possible_actions: List[Action]) -> int:
        pass


class CLIPlayer(Player):
    def __init__(self, index: int):
        self.index = index

    def choose_action(self, observation: Observation, possible_actions: List[Action]) -> int:
        print(f"Player {self.index}")
        for i, action in enumerate(possible_actions):
            print(f"{i}. {action}")

        while True:
            try:
                action_index = int(input())
                if 0 <= action_index < len(possible_actions):
                    return action_index
            except ValueError:
                print(f"Input value from 0 to {len(possible_actions)}")