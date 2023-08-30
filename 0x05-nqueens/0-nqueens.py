#!/usr/bin/python3
"""
A script  that solves the N queens problem.
"""
import sys


def solve_nqueens(N):
    """
    A script  that solves the N queens problem.
    """
    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)

    N = int(N)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    def is_safe(board, row, col):
        """
        Check if a queen can be placed at the given position
        without conflicting with existing queens
        """
        for i in range(col):
            if board[i] == row or abs(board[i] - row) == abs(i - col):
                return False
        return True

    def print_solution(board):
        """
        Prints the solution board.
        """
        solution = [[col, row] for col, row in enumerate(board)]
        print(solution)

    # def print_solution(board):
    #     """
    #     Prints the solution board.
    #     """
    #     for row in board:
    #         print("".join(["Q" if i == row else "." for i in range(N)]))
    #     print()

    def solve_nqueens_util(col, board):
        """
        solve nqueen helper function
        """
        if col >= N:
            print_solution(board)
            return

        for row in range(N):
            if is_safe(board, row, col):
                board[col] = row
                solve_nqueens_util(col + 1, board)
                board[col] = -1

    board = [-1] * N
    solve_nqueens_util(0, board)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    N = sys.argv[1]
    solve_nqueens(N)
