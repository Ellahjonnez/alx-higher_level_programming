#!/usr/bin/python3

import sys


def solve_nqueens(N):

    def is_safe(board, row, col):
        """ Check if a queen can be placed at the given
        row and column without attacking any other queens
        Check column
        """
        for i in range(row):
            if board[i] == col:
                return False
            """ Check diagonal """
            if abs(board[i] - col) == abs(i - row):
                return False
        return True

    def place_queens(board, row):
        """ Base case:
        If all queens are placed, print the solution
        """
        if row == N:
            print_solution(board)
            return

        """ Recursive case:
        Try placing a queen in each column of the current row
        """
        for col in range(N):
            if is_safe(board, row, col):
                board[row] = col
                place_queens(board, row + 1)

    def print_solution(board):
        """ Print the board configuration as a solution"""
        for i in range(N):
            print(f"{i},{board[i]}", end=' ')
        print()

    """ Check the number of arguments """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    """ Parse and validate the input value of N """
    try:
        N = int(sys.argv[1])
        if N < 4:
            print("N must be at least 4")
            sys.exit(1)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    """ Create an empty board """
    board = [0] * N

    """ Solve the N Queens problem """
    place_queens(board, 0)


""" Run the program """
solve_nqueens(0)
