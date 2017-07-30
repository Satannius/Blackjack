"""Player module"""

import card
import stack

class Player(object):
    """Player class"""

    def __init__(self, Stack, Id_num):
        self.name = "PLAYER " + str(Id_num)
        self.playing = False
        self.score = 0
        self.stack = Stack

    def action(self):
        """Performs an action based on user input."""

        p_input = str.upper(raw_input("Draw or pass? Enter 'd' or 'p' and press return. "))

        if p_input == "D":
            draw_card = self.stack.draw()
            self.evaluate(draw_card)
        elif p_input == "P":
            self.playing = False
        else:
            print "Invalid input. "
            self.action()

    def evaluate(self, drawn_card):
        """Evaluates the drawn card."""
        self.score += drawn_card.value
        print "Score: ", self.score
        if self.score > 21:
            print "You've lost!"
            self.playing = False

    def turn(self):
        """Controls turn-flow."""
        self.playing = True

        print self.name
        while self.playing:
            self.action()
