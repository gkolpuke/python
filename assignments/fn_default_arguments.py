#Default arguments
def defaultArgs(a,b,c=3):
    return a+b+c

if(__name__=='__main__'):
    print('Addition number\n')
    x,y = eval(input('Enter 2 numbers by comma separted: '))
    result = defaultArgs(x,y)
    #Here we haven't passed 3 arguments It has default value
    print('Addition is= '+str(result))

    x,y,z = eval(input('Enter 3 numbers by comma separted: '))
    result = defaultArgs(x,y,z)
    print('Addition is= '+str(result))
