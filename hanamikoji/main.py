from hanamikoji.game import Game
from hanamikoji.player import CLIPlayer
from hanamikoji.state import State


def main():
    state = State()
    players = [CLIPlayer(0), CLIPlayer(1)]
    while not state.is_finished():
        print(state)
        actions = Game.get_available_actions(state)
        action_index = players[state.current_player].choose_action(state.observation(), actions)
        action = actions[action_index]
        Game.apply_action(state, action)


if __name__ == "__main__":
    main()
