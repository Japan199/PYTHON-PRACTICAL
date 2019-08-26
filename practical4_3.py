import random
string = ""
print("\ntype \"exit\" to terminate")
x = random.randint(1,10)
reset = False
while 1:
    if reset == True:
        x=random.randint(1,10)
        reset = False
    print(x)

    guess=input("\nEnter your guess : ")
    if guess == "exit":
        print("\t\t******  See Ya  ******")
        break

    if guess.isnumeric():
        guess_int = int(guess)
        #print(guess_int)
        if guess_int == x :
            print("exactly right")
            reset = True
        else:
            if guess_int > x :
                print("high ")
            else:
                print("low")

    else:
        print("Enter valid input")