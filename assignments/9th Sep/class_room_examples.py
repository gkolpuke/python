#!/usr/bin/python
def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def main():
    x,y = eval(input('Enter 2 number: '))
    print('Result of x+y = %d'%add(x,y))

if(__name__=='__main__'):
    print('Running as standalone script',__name__)
    main()
else:
    print('Loaded as module',__name__)
