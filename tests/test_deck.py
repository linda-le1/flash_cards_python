import unittest
from lib.card import Card
from lib.deck import Deck

class TestingDeck(unittest.TestCase):

    def test_it_exists(self):
        category_1 = {"category" : "Geography" }
        card_1 = Card("What is the capital of Alaska?", "Juneau", category_1)
        category_2 = {"category" : "Art"}
        card_2 = Card("Who painted Starry Night?", "Vincent Van Gogh", category_2)
        category_3 = {"category" : "STEM"}
        card_3 = Card("The Viking spacecraft sent back to Earth photographs and reports about the surface of which planet?", "Mars", category_3)
        deck = Deck([card_1, card_2, card_3])
        assert isinstance(deck, Deck)

    def test_cards_exist_in_deck(self):
        category_1 = {"category" : "Geography" }
        card_1 = Card("What is the capital of Alaska?", "Juneau", category_1)
        category_2 = {"category" : "Art"}
        card_2 = Card("Who painted Starry Night?", "Vincent Van Gogh", category_2)
        category_3 = {"category" : "STEM"}
        card_3 = Card("The Viking spacecraft sent back to Earth photographs and reports about the surface of which planet?", "Mars", category_3)
        deck = Deck([card_1, card_2, card_3])
        assert deck.cards == [card_1, card_2, card_3]

if __name__ == '__main__':
    unittest.main()