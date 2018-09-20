'''
		a. Number Pyramid
			      1
			    2 1 2
			  3 2 1 2 3
			4 3 2 1 2 3 4

'''

def pyramid_no(rows):
    for i in range(1, rows+1):
        k = i
        #for space
        for _ in range(rows - i):
            print(' ', end='')
        for j in range(i*2-1):
            #print(j,end='*')
            print(k,end='')
            if( i <= j + 1 ):#here j starts with 0 thats the reason we have added 1 at the time of comparision
                k += 1
            else:
                k -= 1
        print('')

if(__name__ == '__main__'):
    row_count = eval(input('Enter no of rows: '))
    pyramid_no(row_count)
