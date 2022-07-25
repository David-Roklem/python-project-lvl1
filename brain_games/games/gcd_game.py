from random import randint
from math import gcd
from prompt import string
from ..scripts.common_logic import NAME


def play_gcd_game():
    print('Find the greatest common divisor of given numbers.')
    for _ in range(3):
        a = randint(1, 50)
        b = randint(1, 50)
        correct_answer = str(gcd(a, b))
        print(f'Question: {a} {b}')
        user_answer = string('Your answer: ')
        if correct_answer == user_answer:
            print('Correct!')
        else:
            return print(f"{user_answer} is wrong answer ;(. "
                         f"Correct answer was {correct_answer}."
                         f"\nLet's try again, {NAME}!")

    print(f'Congratulations, {NAME}!')
