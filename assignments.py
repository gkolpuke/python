#Assignments
# Date : 25Aug2018
'''W.A.P to accept two numbers from user and display their power'''
print('\n --- Power --- ')
number = eval(input('Enter number: '))
power = eval(input('Enter power of: '))

result = number ** power
print(power,'th of Power', number,' is = ', result )

''' 2nd program
W.A.P. to accept string from  user and print it in reverse order.
'''
print('\n --- Reverse String --- ')
strString = input('Enter a string: ')
revString = strString[::-1]
print('Reverse string is: ' + revString)

# Date : 26Aug2018
'''1- W.A.P to accept a string from user & display a string of first 2 characters & last 2 characters'''
print('\n--**26th Aug 2018**---')
print(' --- first 2 & last 2 charcters --- ')
str1 = input('Enter string: ')
result = str1[:2] + str1[-2:]
print('Resut of two string is = ' + result)

'''
2) W.A.P to accept a string from user & replace the occurance of first charcter in remaning part of string with "*"
  example-
    "babble" O/P => "ba**le"
'''
print('\n---replace first character string occurances with "*" ')
str1 = input('Enter string: ')
result = str1.replace(str1[:1],'*').replace('*',str1[:1],1)
print('replaced string is ' + result)

'''
3) W.A.P to accept a 2 string from user & jumble them
  example-
    'Dog' & 'Dinner'
    O/P=> 'Dig' & Donner
    { swap the first 2 charcters of first string with second string & second string with first string }
'''
print('\n---Jumble two strings---')
str1 = input('Enter first string: ')
str2 = input('Enter second string: ')
print('\nResult - jumbled string')
print('First String: '+ str1[:2] + str2[2:])
print('Second String: ' + str2[:2] + str1[2:])

'''
4) W.A.P to accept a 2 string from user & check if second string is right rotation or not
  example-
    'Manager' & 'germana'
    { True -- mana ger }
'''
print('\n---Right rotation---')

'''
5) W.A.P to accept a string from user & replace 'not bad' with 'good'
'''
print('\n---Replace string---')
