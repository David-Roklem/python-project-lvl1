from prompt import string


def launch_game(play_game, GUIDE):
    print('Welcome to the Brain Games!')
    name = string('May I have your name? ')
    print(f'Hello, {name}!')
    print(GUIDE)
    ROUNDS = 3
    for _ in range(ROUNDS):
        question, correct_answer = play_game()
        print(f'Question: {question}')
        user_answer = string("Your answer: ")
        if user_answer != correct_answer:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'."
                  f"\nLet's try again, {name}!")
            break
        else:
            print('Correct!')
    else:
        print(f'Congratulations, {name}!')

