# Your solution to Exercise 13
n = input()
string = ''
num =  '0123456789'
for i in n:
    if i in num:
        string += i
print(string)