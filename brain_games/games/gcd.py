from random import randint
from math import gcd


GUIDE = 'Find the greatest common divisor of given numbers.'


def generate_round():
    random_number1 = randint(1, 50)
    random_number2 = randint(1, 50)
    question = f'{random_number1} {random_number2}'
    correct_answer = str(gcd(random_number1, random_number2))
    return question, correct_answer
