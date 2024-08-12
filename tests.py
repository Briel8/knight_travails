import unittest
from knight_travails import Board

class BoardTestCases(unittest.TestCase):

    def setUp(self):
        self.board = Board(8)

    def test_valid_move_to_be_true(self):
        """Is (2,1) a valid move?"""
        self.assertTrue(self.board.is_valid_move((2,1)))

    def test_valid_move_to_be_false(self):
        """Is (-1,2) a valid move?"""
        self.assertFalse(self.board.is_valid_move((-1,2)))

    def test_valid_move_to_be_false_1(self):
        """Is (8,2) a valid move?"""
        self.assertFalse(self.board.is_valid_move((8,2)))

    def test_valid_move_to_be_false_2(self):
        """Is (2,8) a valid move?"""
        self.assertFalse(self.board.is_valid_move((2,8)))


if __name__ == "__main__":
    unittest.main()