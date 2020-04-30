import unittest
from lib.card import Card
from lib.deck import Deck
from lib.turn import Turn

class TestingTurn(unittest.TestCase):

    def test_it_exists(self):
        category_1 = {"category" : "Geography" }
        card_1 = Card("What is the capital of Alaska?", "Juneau", category_1)
        turn_1 = Turn("Juneau", card_1)
        assert isinstance(turn_1, Turn)

    def test_it_has_attributes(self):
        category_1 = {"category" : "Geography" }
        card_1 = Card("What is the capital of Alaska?", "Juneau", category_1)
        turn_1 = Turn("Juneau", card_1)
        assert turn_1.guess == "Juneau"

if __name__ == '__main__':
    unittest.main()