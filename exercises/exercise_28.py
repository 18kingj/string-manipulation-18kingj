# Your solution to Exercise 28
n = input()
n = n.strip()
count = 0
for i in n:
    if i == ' ':
        count += 1
print(count + 1)