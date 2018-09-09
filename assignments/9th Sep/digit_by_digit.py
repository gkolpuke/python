#!/usr/bin/python
def digit_by_digit(x):
    if(x==0):
        return 0
    elif(x<10 and x>-10):
        return x

    if(x<0):
        x = -x
    tempList = []
    while(x > 0):
        rem = int(x%10)
        x = int(x/10)
        tempList.append(rem)
    #tempList.append(x)
    return tempList[::-1]

def main():
    x = eval(input('Enter number: '))
    result = digit_by_digit(x)
    print('{} Digit by digit = {}'.format(x,result))

if(__name__=='__main__'):
    print('Running as standalone script',__name__)
    main()
else:
    print('Loaded as module',__name__)
