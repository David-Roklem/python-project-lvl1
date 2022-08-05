from prompt import string


def launch_game(play_calc_game, message):
    print('Welcome to the Brain Games!')
    NAME = string('May I have your name? ')
    print(f'Hello, {NAME}!')
    print(message)
    for _ in range(3):
        question, correct_answer = play_calc_game()
        print(f'Question: {question}')
        user_answer = string("Your answer: ")
        if user_answer == correct_answer:
            print('Correct!')
        else:
            return print(f"'{user_answer}' is wrong answer ;(. "
                         f"Correct answer was '{correct_answer}'."
                         f"\nLet's try again, {NAME}!")
    print(f'Congratulations, {NAME}!')
