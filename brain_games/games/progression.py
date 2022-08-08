from random import randint
from random import choice


GUIDE = 'What number is missing in the progression?'


def play_progression_game():
    progression = list(range(randint(1, 10),
                             randint(35, 50), randint(2, 5)))
    if len(progression) > 10:
        del progression[10::]
    correct_answer = choice(progression)
    for i, n in enumerate(progression):
        if progression[i] == correct_answer:
            progression[i] = '..'
    progression = ' '.join(str(i) for i in progression)
    correct_answer = str(correct_answer)
    return progression, correct_answer
