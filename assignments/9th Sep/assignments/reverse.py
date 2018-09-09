#!/usr/bin/python
#Reverse number
def reverse_number(no):
    if(no<10):
        return no

    reverseNumber = 0
    while(no>0):
        rem = int(no%10)
        reverseNumber = ( reverseNumber * 10 ) + rem
        no = int(no/10)
    return reverseNumber

def main():
    print('Reverse Number\n')
    x = eval(input('Enter number : '))
    result = reverse_number(x)
    print('{} reverse number is {}'.format(x,result))


if(__name__=='__main__'):
    print('Running as standalone script',__name__)
    main()
else:
    print('Loaded as module',__name__)
