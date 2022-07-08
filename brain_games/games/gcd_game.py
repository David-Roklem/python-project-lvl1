from random import randint
from prompt import string
from math import gcd

print('Welcome to the Brain Games!')
NAME = string('May I have your name? ')
print(f'Hello, {NAME}!')


def play_gcd_game():
    print('Find the greatest common divisor of given numbers.')
    for _ in range(3):
        a = randint(1, 50)
        b = randint(1, 50)
        res = gcd(a, b)
        print(f'Question {a} {b}')
        user_answer = string('Your answer: ')
        if res == int(user_answer):
            print('Correct!')
        else:
            return print(f"{user_answer} is wrong answer ;(. Correct answer was {res}.\n Let's try again, {NAME}!")

    print(f'Congratulations, {NAME}!')
