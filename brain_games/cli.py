import prompt

def welcome_user():
	name = prompt.string('May I have your name? ')

welcome_user()

print(f'Hello, {name}!')
