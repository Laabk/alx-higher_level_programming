#!/usr/bin/python3
import sys


def is_safe(board, row, col):
    """ensure that is  safe to place a queen at board[row][col]"""
    # Check the row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i, j = row, col
    while i < N and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def solve_nqueens(board, col):
    """using the recursive mode to solve the N Queens problem"""
    if col >= N:
        solution = [[r, c] for c, r in enumerate(board)]
        print(solution)
        return True

    for row in range(N):
        if is_safe(board, row, col):
            board[row][col] = 1

            solve_nqueens(board, col + 1)

            board[row][col] = 0

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if N < 4:
    print("N must be at least 4")
    sys.exit(1)

# Creating empty chessboard
chessb = [[0 for _ in range(N)] for _ in range(N)]
solve_nqueens(chessb, 0)
