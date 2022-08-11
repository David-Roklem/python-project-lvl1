from random import randint
from random import choice
from operator import add, sub, mul


GUIDE = 'What is the result of the expression?'


def play_game():
    operators = ['+', '-', '*']
    first_operand = randint(1, 100)
    second_operand = randint(1, 100)
    random_operator = choice(operators)
    if random_operator == '+':
        correct_answer = (add(first_operand, second_operand))
    elif random_operator == '-':
        correct_answer = (sub(first_operand, second_operand))
    elif random_operator == '*':
        correct_answer = (mul(first_operand, second_operand))
    question = f'{first_operand} {random_operator} {second_operand}'
    return question, str(correct_answer)
