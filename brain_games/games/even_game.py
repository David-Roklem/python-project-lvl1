from random import randint
from prompt import string
from brain_games.scripts.common_logic import NAME


def play_even_game():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for _ in range(3):
        random_number = randint(1, 100)
        print(f'Question: {random_number}')
        user_answer = string('Your answer: ')
        if random_number % 2 == 0:
            correct_answer = 'yes'
            if user_answer == correct_answer:
                print('Correct!')
            else:
                return print(f"'{user_answer}' is wrong answer ;(. "
                         f"Correct answer was '{correct_answer}'."
                         f"\nLet's try again, {NAME}!")
        elif random_number % 2 != 0:
            correct_answer = 'no'
            if user_answer == correct_answer:
                print('Correct!')
            else:
                return print(f"'{user_answer}' is wrong answer ;(. "
                         f"Correct answer was '{correct_answer}'."
                         f"\nLet's try again, {NAME}!")
    return print(f'Congratulations, {NAME}!')
