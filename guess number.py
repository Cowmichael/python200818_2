import random
num=random.randint(1,10)
i=1
while i<6:
    ans=int(input("write a number:"))
    if ans == num:
        print("you are right")
        print("you played  "+str(i)+"  times")
        break
    elif ans>num:
        print("to big")
        i=i+1    
    elif ans<num:
        print("to small")
        i=i+1
    
          