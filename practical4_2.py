import random
print("press 1 for Stone" )
print("press 2 for scissor")
print("press 3 for paper")
list1=["stone","scissor","paper"]
p1=int(input("Enter the choice : "))
c=random.randint(0,2)
if(c==0):
    print("computer has selected stone : ")
if(c==1):
    print("computer has selected scissor : ")
if(c==2):
    print("computer has selected paper : ")
if p1==1 and c==0:
    print("TIE")
if p1==1 and c==1:
    print("YOU WON")
if p1==1 and c==2:
    print("LOST")
if p1==2 and c==0:
    print("LOST")
if p1==2 and c==1:
    print("TIE")
if p1==2 and c==2:
    print("YOU WON")
if p1==3 and c==0:
    print("YOU WON")
if p1==3 and c==1:
    print("LOST")
if p1==3 and c==2:
    print("TIE")
