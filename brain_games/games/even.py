from random import randint


GUIDE = 'Answer "yes" if the number is even, otherwise answer "no".'


def play_even_game():
    random_number = randint(1, 100)
    if random_number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return random_number, correct_answer