# Your solution to Exercise 18
n = input()
sum = 1
num = '0123456789'
for i in n:
    if i in num:
        sum *= int(i)
print(sum)