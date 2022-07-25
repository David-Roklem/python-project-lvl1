from random import randint
from random import choice
from ..scripts.common_logic import NAME


def play_calc_game():
    operators = ['+', '-', '*']
    print('What is the result of the expression?')
    for _ in range(3):
        first_operand = randint(1, 100)
        second_operand = randint(1, 100)
        res = f'{first_operand} {choice(operators)} {second_operand}'
        print(f'Question: {res}')
        user_answer = input("Your answer: ")
        correct_answer = str(eval(res))
        if user_answer == correct_answer:
            print('Correct!')
        else:
            return print(f"'{user_answer}' is wrong answer ;(. "
                         f"Correct answer was '{correct_answer}'."
                         f"\nLet's try again, {NAME}!")
    print(f'Congratulations, {NAME}!')
