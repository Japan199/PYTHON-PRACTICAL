def duplicate():
    a=int(input("Enter size of list"))
    b=[]
    print("Enter elements")
    for i in range(0,a):
        c=int(input())
        b.append(c)
    d=[]
    for i in b:
        if(i in d):
            continue
        d.append(i)
    for i in range(0,len(d)):
        print(d[i])

duplicate()