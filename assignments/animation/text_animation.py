
#Flying rocket using time & os module
import os
import time

def animate_text(text):
    textLength = len(text)
    i = 1
    time.sleep(0.6)
    os.system('cls')
    while ( i < textLength+1 ):
        print('\n')
        print(text[0:i])
        i += 1

        time.sleep(0.4)
        os.system('cls')
    


if(__name__=='__main__'):
    strName = input('Enter your name: ')
    animate_text( strName )
else:
    print('Imported module')
