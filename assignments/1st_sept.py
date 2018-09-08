'''
W.A.P. to accept a number from user & print if it is even or odd.
(Without using airthmetic operators)
'''
#need to use bitwise operator
no = eval(input('Enter number: '))
if(no & 1):
    print('Number is odd')
else:
    print('Number '+str(no)+' is even number')

'''
W.A.P. to accept a number from user & check number is multiple of 16 or not.
(Without using airthmetic operators)
'''
no = eval(input('Enter number: '))
if(((no>>4)<<4)==no):
    print('Divisible')
else:
    print('Not')
'''
W.A.P. to accept 3 sides from user & display whether they can form trangle or not
'''
s1, s2, s3 = eval(input('Enter 3 sides value by , seperated: '))

if(s1 > (s2+s3) or s2>(s1+s3) or s3>(s1+s2)):
    print('It forms trangle')
else:
    print('It doesn\'t form trangle')
