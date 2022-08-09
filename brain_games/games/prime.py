from random import randint


GUIDE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


# Создается вложенная функция,
# которая проверяет, является ли число n простым или нет.
def is_prime(n):
    if n <= 1:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n


def play_prime_game():
    random_number = randint(2, 100)
    if is_prime(random_number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return random_number, correct_answer
