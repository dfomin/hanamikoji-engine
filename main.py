from cli_game import CLIGame


def main():
    game = CLIGame.new()
    while not game.is_finished():
        print(game)
        game.update()


if __name__ == "__main__":
    main()
