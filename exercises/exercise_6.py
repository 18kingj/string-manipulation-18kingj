# Your solution to Exercise 6
n = input()
letter = False
number = False
num = '1234567890'
for i in n:
    if i >= 'A' and i <= 'z':
        letter = True
    elif i in num:
        number = True
if letter and number:
    print('Your message includes numbers and letters.')
elif letter:
    print('Your message includes letters only.')
elif number:
    print('Your message includes numbers only.')
        