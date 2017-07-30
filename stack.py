"""Stack module"""

import __main__
import card
import random

class Stack(object):
    """Stack class"""

    def __init__(self):
        self.cards = []

    def draw(self):
        """Returns top card"""
        drawn_card = self.cards.pop()
        return drawn_card

    def shuffle(self):
        """Shuffle a new stack of cards"""

        self.cards[:] = []

        for i in range(1, 5):
            for j in range(1, 14):
                value = j
                if j > 10:
                    value = 10
                new_card = card.Card(value)
                self.cards.append(new_card)

        random.shuffle(self.cards)
