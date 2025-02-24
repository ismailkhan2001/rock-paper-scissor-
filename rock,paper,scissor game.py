import random
comp=0
usp=0
def check(c,u):
    global comp,usp
    if(c=="rock") and (u=="rock") or (c=="paper") and (u=="paper") or (c=="sizer") and (u=="sizer"):
        usp+=1
        comp+=1
        print("match is draw")
        print("user and computer score is :",usp,comp)

    elif(c=="rock") and (u=="sizer") or (c=="sizer") and (u=="paper") or (c=="paper") and (u=="rock"):
        if(usp==0):
            usp=0
            comp+=1
            print("you lost the match")
            print("user and computer score is :",usp,comp)
        else:
            usp-=1
            comp+=1        
            print("you lost the match")
            print("user and computer score is :",usp,comp)

    elif(comp==0):
        comp=0
        usp+=1
        print("you won the match")
        print("user and computer score is :",usp,comp)
    else:
        usp+=1
        comp-=1
        print("you won the match")
        print("user and computer score is :",usp,comp)
    return comp,usp
 

while True:
    user=input("choose any from rock, paper, sizer or press quit for exit the match:")
    if(user=="quit"):
        print("match is exited")
        break
    elif all(item in user for item in ["rock","paper","sizer"]):
        print("please enter the above string")
        continue
    
    computer=random.choice(["rock","paper","sizer"])
    print("computer choice is :",computer)
    print("user choice is ",user)
    comp,usp=check(computer,user)

if(comp>usp):
    print("computer won the match by :",comp,usp)
else:
    print("user won the match by :",comp,usp)

