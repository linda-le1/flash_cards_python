import unittest
from lib.card import Card
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
        category_2 = {"category": "Art"}
        card_2 = Card("Who painted Starry Night?", "Vincent Van Gogh", category_2)
        category_3 = {"category": "STEM"}
        card_3 = Card("The Viking spacecraft sent back to Earth photographs and reports about the surface of which planet?","Mars", category_3)
        turn_1 = Turn("Juneau", card_1)
        turn_2 = Turn("Monet", card_2)
        turn_3 = Turn("Mars", card_3)
        assert turn_1.guess == "Juneau"
        assert turn_1.card == card_1
        assert turn_2.guess == "Monet"
        assert turn_2.card == card_2
        assert turn_3.guess == "Mars"
        assert turn_3.card == card_3

    def test_it_can_tell_accuracy(self):
        category_1 = {"category": "Geography"}
        card_1 = Card("What is the capital of Alaska?", "Juneau", category_1)
        category_2 = {"category": "Art"}
        card_2 = Card("Who painted Starry Night?", "Vincent Van Gogh", category_2)
        category_3 = {"category": "STEM"}
        card_3 = Card("The Viking spacecraft sent back to Earth photographs and reports about the surface of which planet?","Mars", category_3)
        turn_1 = Turn("Juneau", card_1)
        turn_2 = Turn("Monet", card_2)
        turn_3 = Turn("Mars", card_3)
        assert turn_1.correct() == True
        assert turn_2.correct() == False
        assert turn_3.correct() == True

    def test_it_gives_feedback(self):
        category_1 = {"category": "Geography"}
        card_1 = Card("What is the capital of Alaska?", "Juneau", category_1)
        category_2 = {"category": "Art"}
        card_2 = Card("Who painted Starry Night?", "Vincent Van Gogh", category_2)
        category_3 = {"category": "STEM"}
        card_3 = Card("The Viking spacecraft sent back to Earth photographs and reports about the surface of which planet?","Mars", category_3)
        turn_1 = Turn("Juneau", card_1)
        turn_2 = Turn("Monet", card_2)
        turn_3 = Turn("Mars", card_3)
        assert turn_1.feedback() == "Great job! Correct!"
        assert turn_2.feedback() == "Not quite. Try again!"
        assert turn_3.feedback() == "Great job! Correct!"


if __name__ == '__main__':
    unittest.main()