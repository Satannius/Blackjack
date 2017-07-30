"""Test module"""

import card
import player
import stack

def test_card_value():
    """Test value of card set."""
    card_ = card.Card(1)
    condition = (card_.value == 1)
    print condition

def test_player_turn():
    """Test player methods"""
    stack_ = stack.Stack()
    stack_.shuffle()
    player_ = player.Player(stack_, 1)
    player_.turn()

def test_stack_length():
    """Test length of stack."""
    stack_ = stack.Stack()
    stack_.shuffle()
    condition = (len(stack_.cards) == 52)
    print condition

def run_tests():
    """Run tests."""
    test_card_value()
    test_player_turn()
    test_stack_length()
