from random import randint
from random import choice
from prompt import string
from brain_games.scripts.common_logic import NAME


def play_progression_game():
    print('What number is missing in the progression?')
    for _ in range(3):
        progression = list(range(randint(1, 10),
                                 randint(35, 50), randint(2, 5)))
        if len(progression) > 10:
            del progression[10::]
        correct_answer = choice(progression)
        for i, n in enumerate(progression):
            if progression[i] == correct_answer:
                progression[i] = '..'
        progression = ' '.join(str(i) for i in progression)
        print(f'Question: {progression}')
        user_answer = string('Your answer: ')
        if user_answer == str(correct_answer):
            print('Correct!')
        else:
            return print(f"'{user_answer}' is wrong answer ;(. "
                         f"Correct answer was '{correct_answer}'."
                         f"\nLet's try again, {NAME}!")
    print(f'Congratulations, {NAME}!')
