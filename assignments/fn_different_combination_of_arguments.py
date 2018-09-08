#W.A.P. to accept multiple different combination of passing arguments
def diffArgs(*args,**dArgs):
    #dArgs = is dictionary arguments
    avg, count, resultStr = 0,0,''
    for x in args:
        avg += x
        count += 1
    
    avgRating = avg/count
    #this is for dictionary arguments
    for x in dArgs:
        if(x == 'name'):
            resultStr = resultStr + dArgs[x] +' is your name.'
        elif(x == 'gender'):
            resultStr = resultStr + ' your gender is ' + dArgs[x] +'.'

    return resultStr + 'You have average rating is: ' + str(avgRating)

if(__name__=='__main__'):
    eName,gender = eval(input('Enter your name & gender by comma separted: '))
    w,x,y,z = eval(input('Enter your C,C++,Python,MySQL subject rating out of 10 in integer by comma separted: '))
    result = diffArgs(w,x,y,z,name=eName,gender=gender)
    print(result)
