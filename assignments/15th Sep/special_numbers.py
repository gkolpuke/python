'''
2. Write a program to check the given number is special number
		e.g. 145
			=> 1! + 4! + 5!
			=> 1 + 24 + 120
			=> 145
'''

def factorialNumber(no):
    fact = 1
    for i in range(1,no+1):
        fact = fact * i
    return fact
    
def isSpecialNumber(no):
    if(no<0):
        return False
    inputNum,add = no,0
    while(no>0):
        rem = no%10
        no = no//10
        
        fact = factorialNumber(rem)
        add = add + fact
    if( add == inputNum ):
        return True
    return False
        
intTillThis = eval(input('Enter number: '))
if(isSpecialNumber(intTillThis)):
    print(str(intTillThis) + ' is a special number')
else:
    print(str(intTillThis) + ' is not a special number')
