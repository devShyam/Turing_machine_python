import time
import os

def replace(a,dirr,r_a):
    if(dirr=='L'):
        a[0]=r_a
    else:
        a[1]=r_a
    return(a)
def display_transition(state,a,dirr,r_a):
    if(dirr=="R"):
        dirr="L"
    else:
        dirr="R"
    spaces=" "
    arr=a
    l=80
    shift=3
    indec=1
    n=4
    if dirr=="R":
        z=0
        indec=1
    else:
        z=n-1
        indec=-1
    for k in range(n):
        if(k==0):
            arr=replace(arr,dirr,r_a)
            
        #print("\n\n\n")
        print("-"*l)
        #print("\n")
        spaces=(" "*shift*z)
        c=0
        print(spaces+" "*(l//4),end="")
        for i in arr:
            c+=1
            if(c<=l):
                print(str(i)+" "*(l//10),end="")
        print("")
        print((" "*(l//2-11))+"^")
        print((" "*(l//2-11))+"|")
        print((" "*(l//2-11))+"|")

        print((" "*(l//4))+"-"*(l//2))
        print((" "*(l//4))+"|"+" "*(l//2-2)+"|")
        print((" "*(l//4))+"|"+" "*(l//2-2)+"|")
        print((" "*(l//4))+"|"+" "*(l//4-3)+state+" "*((l//4)-1)+"|")
        print((" "*(l//4))+"|"+" "*(l//2-2)+"|")
        print((" "*(l//4))+"|"+" "*(l//2-2)+"|")
        print((" "*(l//4))+"-"*(l//2))
        #print("\n\n\n")
        print("-"*l)
        
        if(k<4):
            z+=indec
        else:
            print("",end="")

        time.sleep(1)
        os.system('cls')
        os.system('cls')

        
    
#display_transition("A",[2,3,4,5],"L","7")    
   
