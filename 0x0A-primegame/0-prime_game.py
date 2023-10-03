#!/usr/bin/python3
"""
A function that returns name of the player that won the most rounds
"""


def isWinner(x, nums):
    """
    A function that returns name of the player that won the most rounds
    """
    def is_prime(num):
        """
        Check prime numbers
        """
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def play_game(n):
        """
        Create a set of all numbers from 2 to n
        """
        remaining_numbers = set(range(2, n + 1))
        marias_turn = True

        while True:
            prime_found = False
            for num in range(2, n + 1):
                if num in remaining_numbers and is_prime(num):
                    prime_found = True
                    remaining_numbers -= set(range(num, n + 1, num))
                    break

            if not prime_found:
                return "Ben" if marias_turn else "Maria"

            marias_turn = not marias_turn

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = play_game(n)
        if winner == "Maria":
            maria_wins += 1
        elif winner == "Ben":
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
