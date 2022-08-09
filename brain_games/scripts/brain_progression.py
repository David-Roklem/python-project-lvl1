#!/usr/bin/env python

from brain_games import common_logic
from brain_games.games import progression


def main():
    common_logic.launch_game(
        progression.play_progression_game, progression.GUIDE
    )


if __name__ == '__main__':
    main()
