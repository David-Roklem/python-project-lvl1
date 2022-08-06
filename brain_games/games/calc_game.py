from random import randint
from random import choice


message = 'What is the result of the expression?'


def play_calc_game():
    operators = ['+', '-', '*']
    first_operand = randint(1, 100)
    second_operand = randint(1, 100)
    question = f'{first_operand} {choice(operators)} {second_operand}'
    correct_answer = str(eval(question))
    return question, correct_answer
