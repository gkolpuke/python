#!/usr/bin/python
def isPrime(x):
    if(x<2):
        return False
    elif(x==2):
        return True
    elif(x%2==0):
        return False

    halfNum = int(x/2)
    i = 3
    while(i<halfNum):
        if(x%i==0):
            return False
        i += 2
        
    return True

    


def main():
    x = eval(input('Enter number: '))
    if(isPrime(x)):
        print('{} is prime number'.format(x))
    else:
        print('{} is non prime number'.format(x))

if(__name__=='__main__'):
    print('Running as standalone script',__name__)
    main()
else:
    print('Loaded as module',__name__)
