#!/usr/bin/python
#Armstrong number
import reverse
def isArmstrong(no):
    if(no==1 or no ==10):
        return True
    elif(no<10):
        return False

    user_input = no
    resultNumber = 0
    while(no>0):
        rem = int(no%10)
        resultNumber = resultNumber + (rem * rem *rem)
        no = int(no/10)
    if(user_input == resultNumber):
        return True
    return False

def main():
    print('Armstrong Number\n')
    x = eval(input('Enter number : '))
    if(isArmstrong(x)):
        print('{} is armstrong number'.format(x))
    else:
        print('{} is non armstrong number'.format(x))


if(__name__=='__main__'):
    print('Running as standalone script',__name__)
    main()
else:
    print('Loaded as module',__name__)
