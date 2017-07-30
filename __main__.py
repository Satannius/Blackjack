"""Main module."""

# import card
import game
# import stack
import tests

def main():
    """Main function."""

    game_new = game.Game()
    game_new.play()
    # tests.run_tests()

if __name__ == '__main__':
    # execute only if run as the entry point into the program
    main()
