from random import randint
from random import choice
from prompt import string

print('Welcome to the Brain Games!')
NAME = string('May I have your name? ')
print(f'Hello, {NAME}!')


def play_progression_game():
    print('What number is missing in the progression?')
    for _ in range(3):
        progression = list(range(randint(1, 10),
                           randint(35, 50), randint(2, 5)))
        if len(progression) > 10:
            del progression[10::]
        correct_answer = str(choice(progression))
        string_progression = ' '.join(str(i) for i in progression)
        showed_string_progression = string_progression.replace(
            str(correct_answer), '..')
        print(f'Question: {showed_string_progression}')
        user_answer = str(string('Your answer: '))
        if user_answer == correct_answer:
            print('Correct!')
        else:
            return print(f"'{user_answer}' is wrong answer ;(. "
                         f"Correct answer was '{correct_answer}'."
                         f"\nLet's try again, {NAME}!")
    print(f'Congratulations, {NAME}!')
