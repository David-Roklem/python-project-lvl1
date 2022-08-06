#!/usr/bin/env python

from brain_games.games.calc_game import play_calc_game
from brain_games.scripts import common_logic
from brain_games.games.calc_game import message


def main():
    common_logic.launch_game(play_calc_game, message)


if __name__ == '__main__':
    main()
