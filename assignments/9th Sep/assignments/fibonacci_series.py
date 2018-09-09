#!/usr/bin/python
#fibonacci series
def fibonacci(no):
    fibonacci_list = [0,1]
    if(no==1):
        return fibonacci_list
    first,second,temp=0,1,0
    while(True):
        temp = first + second
        if(temp>=no):
            break

        first = second
        second = temp
        fibonacci_list.append(temp)
    return fibonacci_list

def main():
    print('Fibonacci Series up to number\n')
    x = eval(input('Enter number : '))
    result = fibonacci(x)
    print('Fibonacci of {} number is {}'.format(x,result))


if(__name__=='__main__'):
    print('Running as standalone script',__name__)
    main()
else:
    print('Loaded as module',__name__)
