import unittest
from lib.card import Card

class TestingCard(unittest.TestCase):

    def test_it_exists(self):
        category = {"category" : "Geography" }
        card = Card("What is the capital of Alaska?", "Juneau", category)
        assert isinstance(card, Card)

    def test_it_has_a_question(self):
        category = {"category" : "Geography" }
        card = Card("What is the capital of Alaska?", "Juneau", category)
        assert card.question == "What is the capital of Alaska?"

    def test_it_has_an_answer(self):
        category = {"category" : "Geography" }
        card = Card("What is the capital of Alaska?", "Juneau", category)
        assert card.answer == "Juneau"

    def test_it_has_a_category(self):
        category = {"category" : "Geography"}
        card = Card("What is the capital of Alaska?", "Juneau", category)
        assert card.category == {"category" : "Geography" }


if __name__ == '__main__':
    unittest.main()