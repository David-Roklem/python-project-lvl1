from random import randint
from random import choice


GUIDE = 'What is the result of the expression?'


def generate_round():
    operators = ['+', '-', '*']
    first_operand = randint(1, 100)
    second_operand = randint(1, 100)
    random_operator = choice(operators)
    if random_operator == '+':
        correct_answer = first_operand + second_operand
    elif random_operator == '-':
        correct_answer = first_operand - second_operand
    elif random_operator == '*':
        correct_answer = first_operand * second_operand
    question = f'{first_operand} {random_operator} {second_operand}'
    return question, str(correct_answer)
