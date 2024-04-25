# Your solution to Exercise 29
n = int(input())
s = input()
a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
string = ''
for i in s:
    ascii = ord(i)
    for i in range(n):
        ascii += 1
        if chr(ascii) not in a:
            ascii = ord('a')
    string += chr(ascii)
print(string)