#!/usr/bin/env python

from brain_games import engine
from brain_games.games import progression


def main():
    engine.launch_game(
        progression.play_progression_game, progression.GUIDE
    )


if __name__ == '__main__':
    main()
