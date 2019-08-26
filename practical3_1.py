number=int(input("enter the number"))
listRange = list(range(1,number+1))
divisorlist = []
for num in listRange:
             if number%num == 0:
                 divisorlist.append(num)

print(divisorlist)
                         
             
            
