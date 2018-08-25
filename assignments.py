#Assignments
# Date : 25Aug2018
'''W.A.P to accept two numbers from user and display their power'''
number = eval(input('Enter number: '))
power = eval(input('Enter power of: '))

result = number ** power
print(power,'th of Power', number,' is = ', result )

''' 2nd program
W.A.P. to accept string from  user and print it in reverse order.
'''
print('\n\n --- Reverse String --- ')
strString = input('Enter a string: ')
revString = strString[::-1]
print('Reverse string is: ' + revString)
