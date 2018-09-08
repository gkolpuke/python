#W.A.P. to accept multiple numbers from user & show their multilication
def mul(*args):
    mul = 1
    for x in args:
        mul = mul * x
    return mul

if(__name__=='__main__'):
    print('Multiplication of multiple values')
    x,y = eval(input('Enter two number comma separated: '))
    print('Addition of '+str(x)+ ' & '+str(y)+' is = ' +str(mul(x,y)))

    x,y,z = eval(input('Enter 3 number comma separated: '))
    print('Addition of '+str(x)+ ','+str(y) + ' & '+str(z)+' is = ' +str(mul(x,y,z)))
