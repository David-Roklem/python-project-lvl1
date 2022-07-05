from random import randint
from random import choice
from prompt import string

print('Welcome to the Brain Games!')
name = string('May I have your name? ')
print(f'Hello, {name}!')


def play_calc_game():
    operators = ['+', '-', '*']
    print('What is the result of the expression?')
    for _ in range(3):
        first_operand = randint(1, 100)
        second_operand = randint(1, 100)
        res = f'{first_operand} {choice(operators)} {second_operand}'
        print(f'Question: {res}')
        user_answer = input("Your answer: ")
        if int(user_answer) == eval(res):
            print('Correct!')
        else:
            return print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{eval(res)}'.\nLet's try again, {name}")
    print(f'Congratulations {name}')
