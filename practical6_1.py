def fibbo(n):
    prev=0
    next=1
    for _ in range(0,n):
        print(prev)
        prev,next=next,(prev+next)
    return 0
fibbo(10)


