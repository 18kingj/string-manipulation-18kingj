# Your solution to Exercise 9
n = input()
s = n[0]
f = n[-1]
n = f + n[1:-1] + s
print(n)