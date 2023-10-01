from hanamikoji.game import Game
from hanamikoji.player import CLIPlayer


def main():
    game = Game()
    players = [CLIPlayer(0), CLIPlayer(1)]
    while not game.is_finished():
        print(game)
        actions = game.get_available_actions()
        action_index = players[game.state.current_player].choose_action(game.state.observation(), actions)
        action = actions[action_index]
        game.apply_action(action)


if __name__ == "__main__":
    main()
