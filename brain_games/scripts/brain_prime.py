#!/usr/bin/env python

from brain_games import common_logic
from brain_games.games import prime


def main():
    common_logic.launch_game(prime.play_prime_game, prime.GUIDE)


if __name__ == '__main__':
    main()
