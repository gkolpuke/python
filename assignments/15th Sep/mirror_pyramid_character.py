'''
b. Mirror of pyramid of character pattern:
			D C B A B C D
			  C B A B C
			    B A B			
			      A

'''

def pyramid_no(rows,text):
    intVal = ord(text)

    for i in range(1, rows+1):
        k = intVal + rows - i
        #for space
        for _ in range(i-1):
            print(' ', end='')

        for j in range((rows-(i-1))*2-1):
            #print(k,end='*')
            print(chr(k),end='')
            if( j > ((rows-1)-i) ):#here j starts with 0 thats the reason we have added 1 at the time of comparision
                #print('/',end='')
                k += 1
            else:
                #print(':',end='')
                k -= 1
        print('')

if(__name__ == '__main__'):
    row_count = eval(input('Enter no of rows: '))
    text = input('Enter starting alphabate: ')
    pyramid_no(row_count, text)
