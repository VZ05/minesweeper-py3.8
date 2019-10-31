import random,time
import numpy as np

print('START')

while True:

    
    hplan=np.array([[0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0]])
    
    splan=np.array([['_','_','_','_','_','_','_','_','_','_','line 0'],
                    ['_','_','_','_','_','_','_','_','_','_','line 1'],
                    ['_','_','_','_','_','_','_','_','_','_','line 2'],
                    ['_','_','_','_','_','_','_','_','_','_','line 3'],
                    ['_','_','_','_','_','_','_','_','_','_','line 4'],
                    ['_','_','_','_','_','_','_','_','_','_','line 5'],
                    ['_','_','_','_','_','_','_','_','_','_','line 6'],
                    ['_','_','_','_','_','_','_','_','_','_','line 7'],
                    ['_','_','_','_','_','_','_','_','_','_','line 8'],
                    ['_','_','_','_','_','_','_','_','_','_','line 9'],
                    ['0','1','2','3','4','5','6','7','8','9','<-cols']])
    
    for n in range(20):
        hplan[random.randint(0,9),random.randint(0,9)]=1
    
    #game
    
    hcoord=0
    print(splan)
    
    while hcoord==0 : #GAME
        line=int(input("entry line between 0 and 9 (type 10 to mark a bomb):"))
        col=int(input("entry column between 0 and 9 (type 10 to mark a bomb):"))
        if (line or col)<0 or (line or col)>10 : #error
            print("error entries must me in range [0,9] and 10 to mark")

        if line<10 : #normal situation
            hcoord=hplan[line,col]
            # a  b  c
            # d     e
            # f  g  h

            a=0
            b=0
            c=0
            d=0
            e=0
            f=0
            g=0
            h=0
            
            #center
            if (line<=8 and line>=1) and (col<=8 and line>=1) :
                a=hplan[line-1,col-1]
                b=hplan[line-1,col]
                c=hplan[line-1,col+1]
                d=hplan[line,col-1]
                e=hplan[line,col+1]
                f=hplan[line+1,col-1]
                g=hplan[line+1,col]
                h=hplan[line+1,col+1]

            #corners
            if line==0 and col==0 : #up left
                e=hplan[line,col+1]
                g=hplan[line+1,col]
                h=hplan[line+1,col+1]
            if line==0 and col==9 : #up right
                d=hplan[line,col-1]
                f=hplan[line+1,col-1]
                g=hplan[line+1,col]
            if line==9 and col==0 : #bottom left
                b=hplan[line-1,col]
                c=hplan[line-1,col+1]
                e=hplan[line,col+1]
            if line==9 and col==9 : #bottom right
                a=hplan[line-1,col-1]
                b=hplan[line-1,col]
                d=hplan[line,col-1]
            
            #borders
            if line==0 and col!=0 and col!=9 :
                d=hplan[line,col-1]
                e=hplan[line,col+1]
                f=hplan[line+1,col-1]
                g=hplan[line+1,col]
                h=hplan[line+1,col+1]
            if line==9 and col!=0 and col!=9 :
                a=hplan[line-1,col-1]
                b=hplan[line-1,col]
                c=hplan[line-1,col+1]
                d=hplan[line,col-1]
                e=hplan[line,col+1]
            if col==0 and line!=0 and line!=9 :
                b=hplan[line-1,col]
                c=hplan[line-1,col+1]
                e=hplan[line,col+1]
                g=hplan[line+1,col]
                h=hplan[line+1,col+1]
            if col==9 and line!=0 and line!=9 :
                a=hplan[line-1,col-1]
                b=hplan[line-1,col]
                d=hplan[line,col-1]
                f=hplan[line+1,col-1]
                g=hplan[line+1,col]
            
            nbomb=a+b+c+d+e+f+g+h
            splan[line,col]=nbomb #number that will display to the user
        
        elif line==10: #if there is a bomb to place
            xline=int(input("BOMB line between 0 and 9 (type 10 to cancel):"))
            xcol=int(input("BOMB column between 0 and 9 (type 10 to cancel):"))
            splan[xline,xcol]='x'

        print(splan)
    
    if hcoord==1:
        print("YOU LOSE")
        print(hplan)
    elif hcoord==0:
        print("YOU WIN")
        print(hplan)
    
    restart=input('restart ? Y/N\n')
    if restart=='N':
        break
