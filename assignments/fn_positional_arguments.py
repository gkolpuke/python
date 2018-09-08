#Position arguments
def positionArgs(a,b):
    if(a>b):
        return a
    else:
        return b

if(__name__=='__main__'):
    print('Greater number\n')
    x,y = eval(input('Enter 2 numbers by comma separted: '))
    result = positionArgs(x,y)
    #Here postion of a arguments is first & b is second
    print(str(result)+' is greater number')
