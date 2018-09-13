
#pattern

#square pattern
'''
1. Square pattern
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
'''
def square_star_pattern(no):
    print('\nHey we are represnting square star pattern for you!! \n')
    for _ in range(no):
        for _ in range(no):
            print('*', end=' ')
        print('')


'''
2. Hollow Square star pattern
* * * * *
*        *
*        *
*        *
* * * * *
'''
def hollow_square_star_pattern(no):
    print('\nHellow Square pattern\n')
    for i in range(no):
        for j in range(no):
            if(i>0 and i<no-1 and j>0 and j<no-1):
                #this extra condition added for adding one extra space just before printing last element
                if(j==no-2 or j%4==0):
                    print(' ', end=' ')
                print(' ', end=' ')
            else:
                print('*', end=' ')
        print('')


'''
3. Hollow square star pattern with diagnoal
*****
** **
* * *
** **
*****
'''
def hollow_square_star_pattern_with_diagnoal(no):
    print('\nHollow square star pattern with diagnoal\n')
    for i in range(no):
        
        k = i
        if( k > int(no/2) ):
            k = no - k - 1

        #first loop for printing half data
        for _ in range(k,(int(no/2)+1)):
            print('*',end='')

        #second loop for printing space between two loops
        j = (k-1)
        for _ in range((j*2)+1):
            print(' ',end='')#here space doesn't show  proper due to width of space

        #third loop for printing second half data
        if(i==0 or i==no-1):
            k += 1
        for _ in range(k, (int(no/2)+1)):
            print('*',end='')            
        print('')#this is for new line


'''
4. Rhombus star pattern
    *****
   *****
  *****
 *****
*****
'''
def rhombus_star_pattern(no):
    print('\n"Rhombus star pattern"\n')
    for i in range(no):
        #first loop for printing space before printing *
        for _ in range(i+1,no):
            print(' ',end='')

        for _ in range(no):
            print('*',end='')
        print('')


'''
5. Hollow Rhombus Star Pattern
    *****
   *    *
  *    *
 *    *
*****
'''
def hollow_rhombus_star_pattern(no):
    print('\n"Hollow Rhombus Star Pattern"\n')
    for i in range(no):
        #first loop for printing space before printing *
        for _ in range(i+1,no):
            print(' ',end='')

        for j in range(no):
            if(i>0 and i<no-1 and j>0 and j<no-1):
                print(' ',end='')
            else:
                print('*',end='')
        print('')


'''
6. Mirrored Rhombus Star pattern
*****
 *****
  *****
   *****
    *****
'''
def mirrored_rhombus_star_pattern(no):
    print('\n"Mirrored Rhombus Star Pattern"\n')
    for i in range(no):
        for _ in range(i):
            print(' ',end='')

        #second loop for printing actual *
        for _ in range(no):
            print('*',end='')
        print('')#this is for new line


'''
7. Hollow Mirrored Rhombus Star Pattern
*****
 *    *
  *    *
   *    *
    *****
'''
def hollow_mirrored_rhombus_star_pattern(no):
    print('\n"Hellow Mirrored Rhombus Star Pattern"\n')
    for i in range(no):
        #first loop is for space printing
        for _ in range(i):
            print(' ',end='')

        #second loop is for actual * printing
        for j in range(no):
            if( i>0 and i<no-1 and j>0 and j<no-1 ):
                print(' ',end='')
            else:
                print('*',end='')
        print('')#this is for next line


'''
8. Right Triangle Star Pattern
*
**
***
****
*****
'''
def right_triangle_star_pattern(no):
    print('\n"Right Triangle star pattern"\n')
    for i in range(no):
        for _ in range(i+1):
            print('*',end='')
        print('')#for new line


'''
9. Hollow Right Triangle Star Pattern
*
**
* *
*  *
*****
'''
def hollow_right_triangle_star_pattern(no):
    print('\n"Hollow Right Triangle Star Pattern"\n')
    for i in range(no):
        for j in range(i+1):
            if(i>0 and i<no-1 and j>0 and j<i):
                print(' ',end='')
            else:
                print('*',end='')
        print('')#for new line


'''
10. Inverted Right Triangle Star Pattern
*****
****
***
**
*
'''
def inverted_right_triange_star_pattern(no):
    print('\n"Inverted Right Triangle Star Pattern"\n')
    for i in range(no):
        for _ in range(no-i):
            print('*',end='')
        print('')#for new line


'''
11. Pyramid star pattern
    *
   ***
  *****
 *******
*********
'''
def pyramid_star_pattern(no):
    print('\n"Pyramid star pattern"\n')
    for i in range(no):
        #first loop for printing space
        for _ in range(no-i-1):
            print(' ',end='')

        #second loop for printing actual *
        for _ in range((i*2)+1):
            print('*',end='')
        print('')#this is for new line

'''
12. Hollow Inverted Pyramid star pattern
*********
 *        *
  *      *
   *   *
    * *
     *
'''
def hollow_inverted_pyramid_star_pattern(no):
    print('\n"Hollow Inverted Pyramid Star Pattern"\n')
    for i in range(no):
        #first loop for spacing
        for _ in range(i):
            print(' ',end='')

        #second loop for printing actual *
        temp = (no-i)*2-1
        for j in range(temp):
            if(i>0 and i<no-1 and j>0 and j<temp-1):
                print(' ',end='')
            else:
                print('*',end='')
        print('')

'''
13. Half Diamond Star Pattern
*
**
***
****
***
**
*
'''
def half_diamond_star_pattern(no):
    print('\n"Half Diamond Star Pattern"\n')
    for i in range(no*2):
        k = i
        if(i>no):
            k = no - ( i - no )
        for _ in range(k):
            print('*', end='')
        print('')


def main():
    n = eval(input('Enter no of rows: '))
    #square_star_pattern( n )
    #hollow_square_star_pattern( n )
    #hollow_square_star_pattern_with_diagnoal( n )
    #rhombus_star_pattern( n )
    #hollow_rhombus_star_pattern( n )
    #mirrored_rhombus_star_pattern( n )
    #hollow_mirrored_rhombus_star_pattern( n )
    #right_triangle_star_pattern( n )
    #hollow_right_triangle_star_pattern( n )
    #inverted_right_triange_star_pattern( n )
    #pyramid_star_pattern( n )
    #hollow_inverted_pyramid_star_pattern( n )
    half_diamond_star_pattern(n)

#for executing script in both way
if(__name__=='__main__'):
    print('Stand Alone script')
    main()
else:
    print('Imported script')
