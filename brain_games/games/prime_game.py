from random import randint


message = 'Answer "yes" if given number is prime. Otherwise answer "no".'


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
    random_number = randint(2, 100)
    if isPrime(random_number):
        correct_answer = 'yes'
    if not isPrime(random_number):
        correct_answer = 'no'
    return random_number, correct_answer
