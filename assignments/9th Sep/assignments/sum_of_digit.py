#!/usr/bin/python
#Sum of digit number
def sumOfDigit(no):
    listPrime = []
    if(no<10):
        return no
    else:
        add,rem = 0,0
        while(no>0):
            rem = int(no%10)
            add += rem
            no = no/10

    return add

def main():
    print('Sum of digit number\n')
    x = eval(input('Enter number : '))
    result = sumOfDigit(x)
    print('Sum of digit {} is = {}'.format(x,result))


if(__name__=='__main__'):
    print('Running as standalone script',__name__)
    main()
else:
    print('Loaded as module',__name__)
