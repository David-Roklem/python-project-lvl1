from random import randint
from random import choice
from prompt import string

progression = list(range(randint(1, 10),
                           randint(35, 50), randint(2, 5)))
print(type(progression))
if len(progression) > 10:
    del progression[10::]
correct_answer = choice(progression)
print(type(correct_answer))
for i, n in enumerate(progression):
    if progression[i] == correct_answer:
        progression[i] = '..'
progression = ' '.join(str(i) for i in progression)
print(f'Question: {progression}')