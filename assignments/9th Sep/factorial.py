#!/usr/bin/python
def factorial(x):
    result = 1
    if(x==0):
        return result
    elif(x<0):
        return 'Doesn\'t exist'

    while(x>1):
        result = result * x 
        x -= 1

    return result

    


def main():
    x = eval(input('Enter number: '))
    result = factorial(x)
    print('{}! Factorial = {}'.format(x,result))

if(__name__=='__main__'):
    print('Running as standalone script',__name__)
    main()
else:
    print('Loaded as module',__name__)
