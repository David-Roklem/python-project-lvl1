#!/usr/bin/env python

from brain_games.games import calc
from brain_games import common_logic


def main():
    common_logic.launch_game(calc.play_calc_game, calc.GUIDE)


if __name__ == '__main__':
    main()
