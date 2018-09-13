
#Flying rocket using time & os module
import os
import time

def animate_rocket():
    distanceFromTop = 20
    noOfTimes = 100
    while (noOfTimes>0):
        noOfTimes -= 1
        print("\n" * distanceFromTop)
        print("         /\          ")
        print("         ||          ")
        print("         ||          ")
        print("        /||\        ")

        time.sleep(0.2)
        os.system('cls')
        distanceFromTop -= 1
        if( distanceFromTop <0 ):
            distanceFromTop = 20


if(__name__=='__main__'):
    animate_rocket()
else:
    print('Imported module')
