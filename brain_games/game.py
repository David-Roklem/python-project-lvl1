from random import randint
from prompt import string
from brain_games.cli import welcome_user

print('Welcome to the Brain Games!')
name = string('May I have your name? ')
print(f'Hello, {name}!')


def play_game():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    correct_answers = 0
    while i < 3 and correct_answers <= 3:
        random_number = randint(1, 100)
        print(f'Question: {random_number}')
        user_answer = string('Your answer: ')
        if random_number % 2 == 0 and user_answer == 'yes' or random_number % 2 != 0 and user_answer == 'no':
            print('Correct!')
            correct_answers += 1
        else:
            return print(f"'{user_answer}' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, {name}!")
        if correct_answers == 3:
            return print(f'Congratulations, {name}')
        i += 1
