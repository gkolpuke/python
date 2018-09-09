#!/usr/bin/python
#Difference of even and odd digit sum numbers between ranges
''' importing even_and_odd_digit_sum module for using their functionality '''
import even_and_odd_digit_sum

def diffEvenOddDigitSum(no):
    #using function of other modules
    result = even_and_odd_digit_sum.sumOfDigit(no)

    #result will return sum of even no & sum of odd no
    diff = result[0] - result[1]
    return [diff,result[0],result[1]]


def main():
    print('Difference Sum of even and odd number digit\n')
    x = eval(input('Enter number : '))
    result = diffEvenOddDigitSum(x)
    print('Difference of Sum of even digit and sum of odd digit ({1} - {2}) = {0}'.format(result[0],result[1],result[2]))


if(__name__=='__main__'):
    print('Running as standalone script',__name__)
    main()
else:
    print('Loaded as module',__name__)
