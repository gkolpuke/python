#Keyword arguments
def keywordArgs(a,b):
    if(a>b):
        return a
    else:
        return b

if(__name__=='__main__'):
    print('Greater number\n')
    x,y = eval(input('Enter 2 numbers by comma separted: '))
    result = keywordArgs(a=x,b=y)
    #Here arguments has specified by name
    print(str(result)+' is greater number')
    result = keywordArgs(b=x,a=y)
    print(str(result)+' is greater number')
