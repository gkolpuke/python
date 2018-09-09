#!/usr/bin/python
#Palindrome number
import reverse
def isPalindrome(no):
    if(no<10):
        return True
    revNumber = reverse.reverse_number(no)
    if(no == revNumber):
        return True
    return False

def main():
    print('Palindrome Number\n')
    x = eval(input('Enter number : '))
    if(isPalindrome(x)):
        print('{} is palindrome number'.format(x))
    else:
        print('{} is non palindrome number'.format(x))


if(__name__=='__main__'):
    print('Running as standalone script',__name__)
    main()
else:
    print('Loaded as module',__name__)
