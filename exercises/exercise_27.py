# Your solution to Exercise 27
n = input()
count = 0
string = ''
c = ''
for i in n:
    if i == c:
        count += 1
    else:
        if count > 0:
            string += c + str(count)
        c = i
        count = 1
string += c + str(count)
print(string)