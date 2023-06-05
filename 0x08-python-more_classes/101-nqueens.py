#!/usr/bin/python3
"""
N-Queens Module
"""
import sys


def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at board[row][col]
    Args:
        board (list): The current state of the chessboard.
        row (int): The row to check.
        col (int): The column to check.
    Returns:
        bool: True if it's safe to place a queen, False otherwise.
    """
    # Check the left side of the current row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check the upper diagonal on the left side
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check the lower diagonal on the left side
    i = row
    j = col
    while i < N and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def solve_n_queens(board, col):
    """
    Recursive function to solve the N-Queens problem using backtracking.
    Args:
        board (list): The current state of the chessboard.
        col (int): The current column to check.
    """
    # Base case: All queens are placed
    if col >= N:
        print_solution(board)
        return

    # Recursive case: Try placing the queen in each row of the current column
    for i in range(N):
        if is_safe(board, i, col):
            # Place the queen on the current cell
            board[i][col] = 1

            # Recur for the next column
            solve_n_queens(board, col + 1)

            # Backtrack: Remove the queen from the current cell
            board[i][col] = 0


def print_solution(board):
    """
    Prints a valid solution to the N-Queens problem.
    Args:
        board (list): The current state of the chessboard.
    """
    solution = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                solution.append([i, j])
    print(solution)


# Validate the number of arguments
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

# Parse the argument
try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

# Check if N is at least 4
if N < 4:
    print("N must be at least 4")
    sys.exit(1)

# Initialize the chessboard
board = [[0 for _ in range(N)] for _ in range(N)]

# Solve the N-Queens problem
solve_n_queens(board, 0)
