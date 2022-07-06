from random import randint
from prompt import string

print('Welcome to the Brain Games!')
name = string('May I have your name? ')
print(f'Hello, {name}!')


def play_prime_game():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    # Создается вложенная функция, которая проверяет, является ли число n простым или нет.
    def isPrime(n):
        if n % 2 == 0:
            return n == 2
        d = 3
        while d * d <= n and n % d != 0:
            d += 2
        return d * d > n

    for _ in range(3):
        random_number = randint(2, 100)
        print(f'Question: {random_number}')
        user_answer = string('Your answer: ')
        if isPrime(random_number) is True:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        if isPrime(random_number) is True and user_answer == 'yes':
            print('Correct!')
        if isPrime(random_number) is True and user_answer == 'no':
            return print(f"'no' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again, {name}!")
        if isPrime(random_number) is False and user_answer == 'no':
            print('Correct!')
        if isPrime(random_number) is False and user_answer == 'yes':
            return print(f"'yes' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, {name}!")
    print(f'Congratulations {name}!')
