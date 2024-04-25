# Your solution to Exercise 21
n = input()
string = ''
if n[0:2] == '01':
    string += 'January'
elif n[0:2] == '02':
    string += 'February'
elif n[0:2] == '03':
    string += 'March'
elif n[0:2] == '04':
    string += 'April'
elif n[0:2] == '05':
    string += 'May'
elif n[0:2] == '06':
    string += 'June'
elif n[0:2] == '07':
    string += 'July'
elif n[0:2] == '08':
    string += 'August'
elif n[0:2] == '09':
    string += 'September'
elif n[0:2] == '10':
    string += 'October'
elif n[0:2] == '11':
    string += 'November'
elif n[0:2] == '12':
    string += 'December'
string +=' '
string += n[3:5]
string += ', '
string += n[6:]
print(string)