#W.A.P. to accept number from user & show whether number is even or odd
def isEven(no):
    if(no%2==0):
        return True
    else:
        return False

if(__name__=='__main__'):
    print('Check number is even or odd')
    x = eval(input('Enter number: '))
    if(isEven(x)):
        print(str(x)+' is even number')
    else:
        print(str(x)+' is odd number')
