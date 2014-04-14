# -*- coding: utf-8 -*-
__author__ = 'Most Wanted'

import itertools
import pprint
import chardet
import copy
import time
"""
NONE(' ')
Cтена в которой можно просверлить дырочку слева или справа от героя (в зависимости от того, куда он сейчас смотрит)

BORDER('☼')
Далее исходные правильные циферки, а так же те, которыми походил игрок (возможно ошибочные)

ONE...NINE('1...9')
"""

try_board = [
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

try_board2 = [
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


def build_board(bstr):
    board = bstr.split('board=')[1]
    board = board.decode('utf-8').encode("ascii", "ignore").replace(' ', '0')
    return board

def build_board1(board_string):
    size = 9
    board = board_string.split('board=')[1]
    board = board.decode('utf-8').encode("ascii", "ignore")
    print board
    res_board = []
    for i in itertools.count():
        line = board[i*size:(i+1)*size]
        if not line:
            break
        res_board.append(list(line))
    pprint.pprint(res_board)


class Solver(object):
    size = 9
    def __init__(self, matrix_board):
        self.matrix_coff = [[' ' for x in range(self.size)] for x in range(self.size)]
        self.matrix = matrix_board

    @property
    def get_matrix(self):
        return self.matrix

    def in_square(self, row, column, digit):
        si = row - row % 3
        sj = column - column % 3
        for i in range(si, si+3):
            for j in range(sj, sj+3):
                if self.matrix[i][j] == str(digit):
                    return True
        return False

    def in_column(self, column, digit):
        col = [self.matrix[i][column] for i in range(len(self.matrix))]
        return str(digit) in col

    def calculate_potential(self):
        for i, row in enumerate(self.matrix):
            for j, elem in enumerate(row):
                if self.matrix[i][j] != ' ':
                    continue
                potential = []
                for digit in range(1, 10):
                    if (str(digit) not in row) and \
                            (not self.in_column(j, digit)) and \
                            (not self.in_square(i, j, digit)):
                        potential.append(digit)
                self.matrix_coff[i][j] = potential
                #print "potential for [%s, %s] = %s" % (i, j, potential)

    def put_potentional(self):
        flag = False
        for i, row in enumerate(self.matrix_coff):
            for j, cell in enumerate(row):
                if len(cell) == 1 and self.matrix[i][j] == ' ':
                    self.matrix[i][j] = str(cell[0])
                    flag = True
        return flag

    def solve(self):
        while True:
            self.calculate_potential()
            repeat_flag = self.put_potentional()
            if not repeat_flag:
                break


    def __str__(self):
        pprint.pprint(self.matrix)
        return ""


class BackTrackEngine(object):
    """
    Inherit this class from Solver base
    But first, write this class
    """
    def __init__(self, matrix_board):
        self.m_stack = []
        self.board = matrix_board
        self.counter = 0

    def solve_recursion(self, matrix):

        for i, row in enumerate(matrix):
            for j, cell in enumerate(row):
                for digit in self.put_new_digit(matrix, i, j):
                    new_matrix = copy.deepcopy(matrix)
                    self.solve_recursion(new_matrix)

    def solve(self):
        self.m_stack.append(self.board)
        while len(self.m_stack):
            current = self.m_stack.pop()
            #pprint.pprint(current)
            #time.sleep(2)
            if self.is_full(current):
                print current
                return

            for i, row in enumerate(current):
                flag = False
                for j, cell in enumerate(row):
                    for digit in self.put_new_digit(current, i, j):
                        m_copy = copy.deepcopy(current)
                        m_copy[i][j] = digit
                        self.m_stack.append(m_copy)
                        flag = True
                    if flag:
                        break

    def is_full(self, matrix):
        for row in matrix:
            if ' ' in row:
                return False
        return True

    def put_new_digit(self, matrix, i, j):
        # generate a number for this cell
        if matrix[i][j] != ' ':
            raise StopIteration
        for digit in range(1, 10):  # try all digits from 1 to 9
            str_digit = str(digit)
            if self.can_be_here(matrix, i, j, str_digit):
                yield str_digit

    def get_row(self, i):
        return self.board[i]


    def get_column(self, j):
        return [self.board[i][j] for i in range(len(self.board))]

    def in_square(self, matrix, row, column, digit):
        si = row - row % 3
        sj = column - column % 3
        for i in range(si, si+3):
            for j in range(sj, sj+3):
                if matrix[i][j] == str(digit):
                    return True
        return False

    def in_row(self, matrix, row, digit):
        return str(digit) in matrix[row]

    def in_column(self, matrix, column, digit):
        col = [matrix[i][column] for i in range(len(matrix))]
        return str(digit) in col

    def can_be_here(self, matrix, row, column, digit):
        if not self.in_row(matrix, row, digit) and \
                not self.in_column(matrix, column, digit) and \
                not self.in_square(matrix, row, column, digit):
            return True
        return False

    def __str__(self):
        pprint.pprint(self.board)
        return ''


class BestSolver():
    @staticmethod
    def same_row(i, j):
        return (i / 9 == j / 9)

    @staticmethod
    def same_col(i, j):
        return (i - j) % 9 == 0

    @staticmethod
    def same_block(i, j):
        return (i / 27 == j / 27 and i % 9 / 3 == j % 9 / 3)

    def __init__(self, matrix):
        self.result = matrix

    def solve(self):
        self.r(self.result)

    def r(self, a):
        i = a.find('0')
        if i == -1:
            print a

        excluded_numbers = set()
        for j in range(81):
            if self.same_row(i, j) or self.same_col(i, j) or self.same_block(i, j):
                excluded_numbers.add(a[j])

        for m in '123456789':
            if m not in excluded_numbers:
                self.r(a[:i] + m + a[i + 1:])

if __name__ == '__main__':
    k = BestSolver(try_board)
    k.solve()
    """
    s = Solver(try_board)
    s.solve()
    pprint.pprint(s.get_matrix)
    bs = BackTrackEngine(s.get_matrix)

    bs.solve_recursion(s.get_matrix)

    print bs
    """