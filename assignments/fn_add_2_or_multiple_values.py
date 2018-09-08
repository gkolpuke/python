#W.A.P. to accept number from user & show whether number is even or odd
def add(*args):
    sum = 0
    for x in args:
        sum += x
    return sum

if(__name__=='__main__'):
    print('Addition of multiple values')
    x,y = eval(input('Enter two number comma separated: '))
    print('Addition of '+str(x)+ ' & '+str(y)+' is = ' +str(add(x,y)))

    x,y,z = eval(input('Enter 3 number comma separated: '))
    print('Addition of '+str(x)+ ','+str(y) + ' & '+str(z)+' is = ' +str(add(x,y,z)))
