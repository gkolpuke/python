#
def sub(a,b,c,d):
    return (a+b)-(c+d)

#print(sub(10,c=20,b=30,d=40))

''' defalts arguments '''
def slice1(x,start,end=4,step=1):
    return x[start:end:step]

#print(slice1('Gajanan',0,end=6))

#multplie default parameters
def add(a,b,c=0,d=0,e=0,f=0):
    return a+b+c+d+e+f

print('with 2 parameters: '+str(add(3,4)))
print('with 3 parameters: '+str(add(3,4,5)))
print('with 4 parameters: '+str(add(3,4,5,6)))
print('with 5 parameters: '+str(add(3,4,5,6,7)))
print('with 6 parameters: '+str(add(3,4,5,6,7,8)))

#multiplication
print('\nMultiplication')
def mul(a,b,c=1,d=1):
    return (((a*b)*c)*d)

print('with 2 parameters: '+str(mul(3,4)))
print('with 3 parameters: '+str(mul(3,4,5)))
print('with 4 parameters: '+str(mul(3,4,5,6)))


#variable arguments
print('\n Variable arguments')
def variableArgs(*args):
    print(type(args))
    for x in args:
        print(x)

variableArgs()
variableArgs(1)
variableArgs(3,4)
variableArgs(8,9,'Gajanan')
variableArgs('G',89,[1,2,3],'K')


def addVArgs(*args):
    result = 0;
    for x in args:
        result += x
    return result


print('Addition of no of arguments is: ' +str(addVArgs(2,5,6,7)))
print('Addition of no of arguments is: ' +str(addVArgs(12,15,16)))


#Dictionary arguments
def dictAdd(*args,**dargs):
    print(type(args))
    print(type(dargs))

    for x in args:
        print(x)
    print('\nDictionary')
    
    for x in dargs:
        print('Key is ' +str(x)+ ' and his value is '+str(dargs[x]))

dictAdd(1,3,4,name="Gajanan",course="Python")
dictAdd(name="Gajanan",course="Python")
dictAdd(1,3,4)
