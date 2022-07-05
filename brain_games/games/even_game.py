from random import randint
from prompt import string

print('Welcome to the Brain Games!')
name = string('May I have your name? ')
print(f'Hello, {name}!')


def play_even_game():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for _ in range(3):
        random_number = randint(1, 100)
        print(f'Question: {random_number}')
        user_answer = string('Your answer: ')
        if random_number % 2 == 0 and user_answer == 'yes':
            print('Correct!')
        if random_number % 2 == 0 and user_answer != 'yes':
            return print(f"'{user_answer}' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again, {name}!")
        if random_number % 2 != 0 and user_answer == 'no':
            print('Correct!')
        if random_number % 2 != 0 and user_answer != 'no':
            return print(f"'{user_answer}' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, {name}!")
    return print(f'Congratulations, {name}')
