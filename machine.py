import re
from pre_0n1n import *
from display import *
size=100

import os
class Turing:
        
        def __init__(self):
            self.index=0
            self.tape=[]
            self.tf=[] #transiton functions
            self.tape.append(-2) #-2 is B or blank character in tape
            self.tape.append(-2)
        def moveRight():
            index+=1
            return(index)
        def moveLeft():
            if(index-1>=0):
                index-=1
                return(index)
            else:
                print("No tape found at left")

        def currentIndex():
            return(index)

        def updateTape(val):
            i=currentIndex()
            tape[i]=val

        def isBlank():
            if(tape[currentIndex()]==-2):
                return(True)
            else:
                return(False)

        def RUN_machine(self):

                tf1=self.tf
                #replace = with a comma
                for k in range(len(tf1)):
                        tf1[k]=tf1[k].replace(" ","")
                        tf1[k]=tf1[k].replace("=",",")
                        #print(tf1[k])
                indices=[]
                direction=''
                replace_aplha=''
                cur_state="q0"
                copy_state=cur_state
                a_copy=[]
                i=2
                while(i<len(self.tape)-2):
                        ins=[]
                        tape=self.tape
                        #print("Current state:" +cur_state)
                        for j in tf1:
                                #get corresponding instruction
                                loc=(r'{0},{1}'.format(cur_state,self.tape[i]))
                                temp1=j[:4]
                                #print(temp1)
                                boolValue=(loc==temp1)
                                if(boolValue==True):
                                   ins=j
                                   #print(ins)
                                   break
                                
                        #clean the instruction to get further details
                        temp=list((str(ins)).split(','))
                        #print(temp)
                        if(len(temp)>=3):
                                cur_state,replace_alpha,direction=temp[2:]
                        else:
                                print("Not accepted input")
                                return(0)
                        if(direction=="R"):
                                a_copy=tape[i:i+4]
                                #print(a_copy)
                        else:
                                a_copy=tape[i-1:i+3]
                        display_transition(copy_state,a_copy,direction,replace_alpha)
                        copy_state=cur_state
                        self.tape[i]=replace_alpha
                        #print("Next state: "+cur_state)
                        #make a moving turing machine tape
                        if(direction=="R"):
                                i+=1
                                
                        else:
                                i-=1
                                
                        
                        #print("Replaced"+str(self.tape[i])+"to",end="")
                        
                        #print(self.tape[i])
                print("Accepted input")
                return(1)
                        
                
                        
                        

class TOC:

    def input(self,obj):
            print("1 for new machine entry 2 for preloaded machines")
            x=int(input())
            if(x==1):
                    print("Enter the transiiton of the language in the form : (state (Q),input alphabet) =(state (Q'),replaceAlpahbet,MoveDirection)" )
                    print("Example : A,a = B,c,R")
                    print("Example : A,b = C,a,L")
                    print("Enter \"END\" to exit input")
                    x=input()

                    while( x != "END"):
                        obj.tf.append(temp)
                        x=input()

                    
            else:
                    print("Pre loaded turing machine\n 1: n zeros followed by n ones  (O^n1^n)\n2: Palindrome ")
                    choice=int(input())
                    if(choice==1):
                            obj.tf=run_on1n()
                            self.get_tape(obj)
                    else:
                            print("NO inbuilt options found")
   
    def get_tape(self,obj):
            print("Enter the Input String")
            for i in input():                                        
                    (obj.tape).append(int(i))
            (obj.tape).append(-2)
            (obj.tape).append(-2)       
    def  Display(self,obj):
        print("Current State, input alphabet = new state , Replaced alphabet , direction")
        for i in obj.tf:
                if(i==-2):
                        print("B")
                else:
                        print(i)
        print("The given input is:")
        print(obj.tape)

            

def main():
     os.system('cls')
     obj=TOC()
     objT=Turing()
     obj.input(objT)
     
     obj.Display(objT)
     ans=objT.RUN_machine()
main()
