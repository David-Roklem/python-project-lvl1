#!/usr/bin/env python

from brain_games import engine
from brain_games.games import gcd


def main():
    engine.launch_game(gcd.play_gcd_game, gcd.GUIDE)


if __name__ == '__main__':
    main()
