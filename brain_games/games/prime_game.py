from random import randint
from prompt import string
from brain_games.scripts.common_logic import NAME


# Создается вложенная функция,
# которая проверяет, является ли число n простым или нет.
def isPrime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n


def play_prime_game():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    for _ in range(3):
        random_number = randint(2, 100)
        print(f'Question: {random_number}')
        user_answer = string('Your answer: ')
        if isPrime(random_number) is True:
            correct_answer = 'yes'
            if correct_answer == user_answer:
                print('Correct!')
            else:
                return print(f"'{user_answer}' is wrong answer ;(. "
                             f"Correct answer was '{correct_answer}'."
                             f"\nLet's try again, {NAME}!")
        if isPrime(random_number) is False:
            correct_answer = 'no'
            if correct_answer == user_answer:
                print('Correct!')
            else:
                return print(f"'{user_answer}' is wrong answer ;(. "
                             f"Correct answer was '{correct_answer}'."
                             f"\nLet's try again, {NAME}!")
    print(f'Congratulations, {NAME}!')
