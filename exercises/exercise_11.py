# Your solution to Exercise 11
count = -1
n = input()
_ = False
while not _:
    if ' ' not in n:
        break
    if n[count-1] == ' ':
        _ = True
        continue
    count -= 1
if not _:
    print(n)
else:
    n2 = n[count:]
    print(n2)