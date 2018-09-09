#!/usr/bin/python
#List of prime numbers between ranges
def rangePrimeNumber(start,end):
    listPrime = []
    for x in range(start,end+1):
        if(x>=1 and x<=3 ):
            listPrime.append(x)
        elif(x%2==0):
            continue
        else:
            i=3
            halfNum = int(x/2)
            while(i<halfNum):
                if(x%i==0):
                    break
                i += 2
            else:
                listPrime.append(x)

    return listPrime

def main():
    print('Prime number between 2 numbers\n')
    x,y = eval(input('Enter range of number : '))
    result = rangePrimeNumber(x,y)
    print('list is prime number between {}, {} = {}'.format(x,y,result))


if(__name__=='__main__'):
    print('Running as standalone script',__name__)
    main()
else:
    print('Loaded as module',__name__)
