
#pattern

#square pattern
'''
1. Square pattern
    * 
  ***
 *****
*******
 *****
  ***
   *
'''
def diamond_star_pattern(no):
    print('"Diamond Star Pattern"\n')
    for i in range(no*2):
        #first loop for spacing
        sp_range = no-i
        if(i>no):
            sp_range = i - no
        for _ in range(sp_range):
            print(' ',end='')

        #second loop for  printing actual *
        star_range = i*2
        if(i>no):
            star_range = ( no - (i - no) ) * 2
        for _ in range(star_range-1):
            print('*',end='')
        print('')

'''
2. Right Arrow star pattern
*****
 ****
  ***
   **
     *
   **
  ***
 ****
*****
'''
def right_arrow_star_pattern(no):
    print('"Right Arrow star pattern"\n')
    for i in range(no*2-1):
        #first loop for space
        sp_range = i
        if(i>=no):
            sp_range = no - (i - no)-2
        for _ in range(sp_range*3):
            print(' ',end='')

        #second loop for *
        star_range = i
        if( i>=no ):
            star_range = no - ( i - no )-2
        for j in range(star_range,no):
            print('*',end='')
        print('')

def main():
    n = eval(input('Enter no of rows: '))
    #diamond_star_pattern( n )
    right_arrow_star_pattern( n )
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
    #half_diamond_star_pattern(n)

#for executing script in both way
if(__name__=='__main__'):
    print('Stand Alone script')
    main()
else:
    print('Imported script')
