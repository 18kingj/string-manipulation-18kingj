# Your solution to Exercise 30
n = input()
n = n.upper()
sum = 0
p = ''
for i in range(len(n)): 
    if n[i] == 'M':
        sum += 1000
    elif n[i] == 'D':
        sum += 500
    elif n[i] == 'C':
        sum += 100
    elif n[i] == 'L':
        sum += 50
    elif n[i] == 'X':
        sum += 10
    elif n[i] == 'V':
        sum += 5
    elif n[i] == 'I':
        sum += 1
    if p == 'I' and n[i] != 'I':
        sum -= 2
    elif p == 'X' and n[i] != 'I' and n[i] != 'V' and n[i] != 'X':
        sum -= 20
    elif p == 'C' and n[i] != 'I' and n[i] != 'V' and n[i] != 'X' and n[i] != 'L' and n[i] != 'C':
        sum -= 200
    p = n[i]
print(sum)