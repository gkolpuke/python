#!/usr/bin/python
#Sum of even and odd digit number
def sumOfDigit(no):
    if(no<10 ):
        if(no%2==0):
            return [no,0]
        return [0,no]
    else:
        evenSum,oddSum,rem = 0,0,0
        while(no>0):
            rem = int(no%10)
            if(rem%2==0):
                evenSum += rem
            else:
                oddSum += rem
            no = no/10

    return [evenSum,oddSum]

def main():
    print('Sum of even and odd number digit\n')
    x = eval(input('Enter number : '))
    result = sumOfDigit(x)
    print('Sum of even digit is = {} and sum of odd digit is {}'.format(result[0],result[1]))


if(__name__=='__main__'):
    print('Running as standalone script',__name__)
    main()
else:
    print('Loaded as module',__name__)
