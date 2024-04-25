# Your solution to Exercise 25
n = input()
for i in n:
    if i == '\\':
        print('')
        continue
    print(i, end='')