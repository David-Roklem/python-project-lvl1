from random import randint
from math import gcd


message = 'Find the greatest common divisor of given numbers.'


def play_gcd_game():
    a = randint(1, 50)
    b = randint(1, 50)
    question = f'{a} {b}'
    correct_answer = str(gcd(a, b))
    return question, correct_answer
