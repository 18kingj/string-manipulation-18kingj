# Your solution to Exercise 22
n = input()
n = n.replace(' ', '')
n = n.replace(',', '')
n = n.lower()
nr = n[-1::-1]
if n == nr:
    print('Yes')
else:
    print('No')