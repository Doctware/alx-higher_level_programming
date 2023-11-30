#!/usr/bin/python3
import sys


def is_safe(board, row, col, N):
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens_util(board, col, N):
    if col == N:
        print_board(board, N)
        return

    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1  # Place the queen

            solve_nqueens_util(board, col + 1, N)

            board[i][col] = 0


def solve_nqueens(N):
    board = [[0] * N for _ in range(N)]

    solve_nqueens_util(board, 0, N)


def print_board(board, N):
    for i in range(N):
        for j in range(N):
            print("Q" if board[i][j] == 1 else ".", end=" ")
        print()
    print()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])

        if N < 4:
            raise ValueError("N must be at least 4")

        solve_nqueens(N)

    except ValueError:
        print("N must be a number")
        sys.exit(1)
