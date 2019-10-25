import random,time
import numpy as np

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
    
    while hcoord==0:
        line=int(input("entry line between 0 and 9 (type 10 to mark a bomb):"))
        col=int(input("entry column between 0 and 9 (type 10 to mark a bomb):"))
        if (line or col)<0 or (line or col)>10:
            print("error entries must me in range [0,9] and 10 to mark")
        
        
        ten=False
        if line==10:
            ten=True
        if hcoord==0 and ten==False:
            hcoord=hplan[line,col]
            # a  b  c
            # d     e
            # f  g  h
            a=hplan[line-1,col-1]
            b=hplan[line-1,col]
            c=hplan[line-1,col+1]
            d=hplan[line,col-1]
            e=hplan[line,col+1]
            f=hplan[line+1,col-1]
            g=hplan[line+1,col]
            h=hplan[line+1,col+1]
            nbomb=a+b+c+d+e+f+g+h
            splan[line,col]=nbomb
        elif ten==True:
            xline=int(input("BOMB line between 0 and 9 :"))
            xcol=int(input("BOMB column between 0 and 9 :"))
            splan[xline,xcol]='x'
        print(splan)
    
    #end
    
    if hcoord==1:
        print("YOU LOSE")
        print(hplan)
    elif hcoord==0:
        print("YOU WIN")
        print(hplan)
    
    restart=input('restart ? Y/N')
    if restart=='N':
        break

    
    

