'''
Write a program to accept range from user and print armstrong numbers from given range
'''

def armstrongNumber(no):
    if(no>0 and no<10):
        return True
    inputNum,add = no, 0
    noLength = len(str(inputNum))
    while(no>0):
        rem = no%10
        add = add + ( rem ** noLength )
        no = no//10
    #print('inputNum == ' + str(inputNum) + ' ** add == '+str(add))
    if( inputNum == add ):
        return True
    else:
        return False
    
    
def lsitOfArmstrongNumber(tillNo):
    arrArmstrongNumbers = []
    for i in range(1,tillNo+1):#plus 1 for considering that number also
        if( armstrongNumber(i) ):
            arrArmstrongNumbers.append(i)
    
    return arrArmstrongNumbers
        
intTillThis = eval(input('Enter number: '))
arrArmstrongNumbers = lsitOfArmstrongNumber(intTillThis)

print('Armstrong number till '+ str(intTillThis) + ' this number is '+ str(arrArmstrongNumbers))
