__author__ = 'Most Wanted'

import unittest
from logic import BackTrackEngine
class TestSolver(unittest.TestCase):

    def setUp(self):
        self.board = [
            ['5', '3', ' ', '6', ' ', '8', ' ', ' ', '2'],
            [' ', ' ', '2', '1', '9', '5', ' ', ' ', ' '],
            ['1', ' ', '8', '3', '4', ' ', '5', ' ', '7'],
            [' ', ' ', '9', '7', '6', ' ', ' ', ' ', ' '],
            [' ', '2', '6', ' ', ' ', ' ', '7', '9', '1'],
            [' ', '1', ' ', '9', ' ', ' ', ' ', ' ', ' '],
            ['9', '6', '1', ' ', ' ', '7', ' ', ' ', ' '],
            ['2', '8', '7', '4', ' ', ' ', '6', '3', ' '],
            ['3', ' ', '5', ' ', ' ', '6', ' ', '7', '9'],
        ]
        self.full_board_incorrect = [
            ['5', '3', '8', '6', '9', '8', '1', '3', '2'],
            ['5', '3', '8', '6', '9', '8', '1', '3', '2'],
            ['5', '3', '8', '6', '9', '8', '1', '3', '2'],
            ['5', '3', '8', '6', '9', '8', '1', '3', '2'],
            ['5', '3', '8', '6', '9', '8', '1', '3', '2'],
            ['5', '3', '8', '6', '9', '8', '1', '3', '2'],
            ['5', '3', '8', '6', '9', '8', '1', '3', '2'],
            ['5', '3', '8', '6', '9', '8', '1', '3', '2'],
            ['5', '3', '8', '6', '9', '8', ' ', '3', '2'],
        ]

        self.full_board_correct = [

        ]
        self.solver = BackTrackEngine(self.board)

    def test_correct_column(self):
        s = self.solver
        col = ['5', ' ', '1', ' ', ' ', ' ', '9', '2', '3']
        s_col = s.get_column(0)
        self.assertEqual(col, s_col)

    def test_correct_row(self):
        s = self.solver
        row = ['5', '3', ' ', '6', ' ', '8', ' ', ' ', '2']
        s_row = s.get_row(0)
        self.assertEqual(row, s_row)

    def test_full_matrix(self):
        s = self.solver
        m = self.board
        self.assertEqual(s.is_full(m), False)

    def test_correct_matrix(self):
        pass

    def test_digit_in_row(self):
        s = self.solver
        m = self.board
        self.assertEqual(s.in_row(m, 0, 1), False)
        self.assertEqual(s.in_row(m, 0, 5), True)

    def test_digit_in_column(self):
        s = self.solver
        m = self.board
        self.assertEqual(s.in_column(m, 4, 5), False)
        self.assertEqual(s.in_column(m, 4, 6), True)

    def test_digit_in_region(self):
        s = self.solver
        m = self.board
        self.assertEqual(s.in_square(m, 0, 0, 3), True)
        self.assertEqual(s.in_square(m, 2, 4, 9), True)
        self.assertEqual(s.in_square(m, 8, 5, 7), True)
        self.assertEqual(s.in_square(m, 0, 0, 9), False)
        self.assertEqual(s.in_square(m, 2, 4, 2), False)
        self.assertEqual(s.in_square(m, 8, 5, 5), False)

    def test_solving(self):
        pass

    def test_guess(self):
        s = self.solver
        m = self.board
        self.assertEqual(s.can_be_here(m, 0, 0, 1), False)
        self.assertEqual(s.can_be_here(m, 0, 2, 1), False)
        self.assertEqual(s.can_be_here(m, 0, 2, 4), True)
        for i in range(9):
            for j in range(9):
                print list(s.put_new_digit(m, i, j))

