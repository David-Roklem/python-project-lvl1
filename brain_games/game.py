first_sentence = 'Answer "yes" if the number is even, otherwise answer "no".'

print(first_sentence)

a = int(input('Question: '))

if a % 2 == 0:
    print('yes')
else:
    print('no')
