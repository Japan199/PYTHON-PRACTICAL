def iprime():
    a=int(input("Enter number"))
    flag=0
    for i in range(2,a-1):
        if((a%i)==0):
            flag=1
    if(flag==1):
        print("Number is not prime")
    elif(flag==0):
        print("Number is prime")

iprime()