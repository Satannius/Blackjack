"""Game module."""

import card
import player
import stack

class Game(object):
    """Game class"""

    def __init__(self):
        self.players = []
        self.cards = stack.Stack()
        self.cards.shuffle()

    def setup(self):
        """Setup the game and variable parameters."""

        playercount = 0

        while True:
            try:
                p_input = raw_input("Enter number of players (2-4) and press return.\n")
                playercount = int(p_input)
                break
            except ValueError:
                print "Invalid input. "

        if playercount < 2 or playercount > 4:
            print "Invalid input. "
            self.setup()
        else:
            for i in range(0, playercount):
                self.players.append(player.Player(self.cards, (i+1)))

    def run(self):
        """Runs the game as specified during setup."""
        winning_score = 0
        winner = "... no one! Everyone lost!"

        for i in range(0, len(self.players)):
            self.players[i].turn()

        for i in range(0, len(self.players)):
            if self.players[i].score < 22 and self.players[i].score > winning_score:
                winning_score = self.players[i].score
                winner = self.players[i].name

        print "The winner is ", winner

    def play(self):
        """Play Blackjack."""

        self.setup()
        self.run()
