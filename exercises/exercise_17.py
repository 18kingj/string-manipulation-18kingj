# Your solution to Exercise 17
n = input()
n = n.strip()
space = 0
for i in n:
    if i == ' ':
        space += 1
print(space+1)