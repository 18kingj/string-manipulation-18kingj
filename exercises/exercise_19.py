# Your solution to Exercise 19
n = input()
num = 0
for i in range(len(n)):
    if n[i] == '.':
        num = n[i+1]
print(num)