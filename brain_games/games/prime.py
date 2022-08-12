from random import randint


GUIDE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


# Создается вложенная функция,
# которая проверяет, является ли число n простым или нет.
def is_prime(n):
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            return False
    return True


def play_game():
    random_number = randint(2, 100)
    if is_prime(random_number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return random_number, correct_answer
