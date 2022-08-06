#!/usr/bin/env python

from brain_games.games.even_game import play_even_game
from brain_games.scripts import common_logic
from brain_games.games.even_game import message


def main():
    common_logic.launch_game(play_even_game, message)


if __name__ == '__main__':
    main()
