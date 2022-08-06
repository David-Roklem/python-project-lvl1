#!/usr/bin/env python

from brain_games.games.gcd_game import play_gcd_game
from brain_games.scripts import common_logic
from brain_games.games.gcd_game import message


def main():
    common_logic.launch_game(play_gcd_game, message)


if __name__ == '__main__':
    main()
