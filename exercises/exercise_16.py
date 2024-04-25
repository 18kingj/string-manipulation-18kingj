# Your solution to Exercise 16
n = input()
s = input()
na = ord(n)
sa = ord(s)
if na > sa:
    for i in range(sa, na + 1):
        print(chr(i), end="")
else:
    for i in range(na, sa + 1):
        print(chr(i), end="")