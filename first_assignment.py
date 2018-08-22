print('Date: 18Aug2018')

#Take two number from user and do thier addition

intFirstNumber = input('Enter first value: ')
intSecondNumber = input('Enter second value: ')

result = int(intFirstNumber) + int(intSecondNumber)
print('Addition of two number is : ', result )



strName = input('Enter Your Name: ')
print('Hello ', strName, '\n')

# W.A.P. to accept two numbers & show their addition
print('Addition of two numbers:')
intFirstNumber = int( input('Enter first number: ') )
intSecondNumber = int( input('Enter second number: ') )
intAddition = intFirstNumber + intSecondNumber
print('Addition of two number is ',intAddition)


#W.A.P to accept string from user & accept the start index, end index and slicing index and display the result of string
print('\nString slicing\n')

strString = input('Enter string: ')
intStratIndex = int(input('Enter strat Index: '))
intEndIndex = int(input('Enter End Index: '))
intSlicingChar = int(input('Enter slicing Index: '))

print(strString[intStratIndex:intEndIndex:intSlicingChar])