#function base programs
#w.a.p. to accept a no. from user & check whether no is multiple of 128 or not using bitwise operator

def isDivisible128(no):
    if(no<0 or no<=128):
        return False
    elif((no & 127)==0):
        return True
    else:
        return False
'''
no1 = eval(input('Enter number: '))
result = isDivisible128(no1)
if(result):
    print('Entered no '+str(no1)+' is divisible of 128')
else:
    print('Entered no '+str(no1)+' is not divisible of 128')
'''

#w.a.p to accept three no from user and print maximum out of them
def maximum( a, b, c ):
    if(a>b and a>c):
        return a
    elif(b>c):
        return b
    else:
        return c

def minimum( a, b, c ):
    if(a<b and a<c):
        return a
    elif(b<c):
        return b
    else:
        return c

#w.a.p. to accept a number from user, if it is less than or equl to 2 then print too few donates. If it is between 3 to 10 then display no ofdonates value
#If the values is greater than 10 then display no of donates too many

def donatesQty( n ):
    if(n<=2):
        return 'too few donates'
    elif(n<10):
        return 'no of donates is ' + str(n)
    else:
        return 'no of donates too many'

#returing binary number representation
def binaryForm( n ):
    arr = []
    flag = True
    i = 1
    while(flag==True):
        no = 2**i
        i += 1
        if(no > n):
            break
        arr.append(no)
    return arr

no1, no2, no3 = eval(input('Enter three numbers: '))
#print('Maximum number is', maximum(no1,no2,no3))
#print('Minimum number is', minimum(no1,no2,no3))

#print('Donates output === '+ donatesQty(no1))

print(binaryForm( no1 ))
