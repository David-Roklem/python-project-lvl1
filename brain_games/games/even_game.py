from random import randint
from prompt import string

print('Welcome to the Brain Games!')
NAME = string('May I have your name? ')
print(f'Hello, {NAME}!')


def play_even_game():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for _ in range(3):
        random_number = randint(1, 100)
        print(f'Question: {random_number}')
        user_answer = string('Your answer: ')
        if random_number % 2 == 0 and user_answer == 'yes':
            print('Correct!')
        if random_number % 2 == 0 and user_answer != 'yes':
            return print(f"'{user_answer}' is wrong answer ;(. "
                         f"Correct answer was 'yes'."
                         f"\nLet's try again, {NAME}!")
        if random_number % 2 != 0 and user_answer == 'no':
            print('Correct!')
        if random_number % 2 != 0 and user_answer != 'no':
            return print(f"'{user_answer}' is wrong answer ;(. "
                         f"Correct answer was 'no'."
                         f"\nLet's try again, {NAME}!")
    return print(f'Congratulations, {NAME}!')
