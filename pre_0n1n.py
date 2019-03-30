#computes if input is 0s followed by 1s or  NOT:
#input alphabets a,b

def  run_on1n():
    #the transition instructions
    #A,a=B,b,R
    #states= 0,1,2,3,4,5
    #inputs 0,1
    #directions L R

    trans=["q0,0 = q1,X,R ","q1,0 = q1,0,R","q1,Y = q1,Y,R",
            "q1,1 = q2,Y,L","q2,Y = q2,Y,L","q2,0 =q2,0,L",
            "q2,X = q0,X,R","q0,Y=q3,Y,R","q3,Y=q3,Y,R","q3,B=q4,B,R" ]
    return(trans);
    #run macgine
