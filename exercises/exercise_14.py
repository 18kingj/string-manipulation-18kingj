# Your solution to Exercise 14
n = input()
n = n.strip()
np = ''
string = ''
for i in range(len(n)):
    if n[i] == ' ':
        if np == ' ':
            np = n[i]
            continue
        elif n[i:] == '   .':
            string += '.'
            break
    string += n[i]
    np = n[i]
print(string)