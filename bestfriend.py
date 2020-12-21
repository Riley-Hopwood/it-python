#!/usr/bin/python

print('+-----------------+')
print('|Best friend maker|')
print('|    By Riley     |')
print('+-----------------+')
print('')
print("Hi. I'm the computer.")

while True:
    name = input('What is your name?')
    color = input(f'Hi {name}. What is your favorite color?')
    print(f'No way! My favorite color is also {color}!')

    movie = input('what is your favorite movie?')
    print(f'What!?! My favorite movie is also {movie}')

    game = input('what is your faorite game')
    print(f'Get out of here! My favorite game is {game}, too')
    print('We like the same things! We should be friends!')
    print('')
    
    response = input('would you like to go again? (Y/n) ')
    while response.lowe() not in ['n', 'no', 'nope','y','yes','yep']:
        response = input('would you like to go again? (Y/n) ')
    if response.lower() in ['n','no', 'nope', 'nu-uh']:
        break