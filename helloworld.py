#!/usr/bin/python

print('+--------------+')
print('|  HELLO WORLD |')
print('|   By Riley   |')
print('+--------------+')
print('')

name = input('What is your name?')
age = input('what is your age? ')
if age.isnumeric():
    age = int(age)
    print(f'Hello {name}. You are {age} years old')
    print(f'Next year, you will be {age+1} years old')
else:
    print("you didn't type a valid number")