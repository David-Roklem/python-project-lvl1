#!/usr/bin/env python

from brain_games import engine
from brain_games.games import even


def main():
    engine.launch_game(even.play_even_game, even.GUIDE)


if __name__ == '__main__':
    main()
