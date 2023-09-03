from game import Game
from player import CLIPlayer


class CLIGame:
    @staticmethod
    def new() -> Game:
        players = [CLIPlayer(0), CLIPlayer(1)]
        return Game(players)
