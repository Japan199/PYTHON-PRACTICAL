a=[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
list1=[x for x in range(2,51)]
b=[element for element in range(len(a))  if element % 2 == 0]
square_odd=[x**2 for x in range(1,11) if x%2 != 0]
power=[2**x for x in range(1,11)]
prime=[x for x in range(2,51) if all(x%y!=0 for y in range(2,x))]
non_prime=list(set(list1)-set(prime))
print(b)
print(square_odd)
print(power)
print(prime)
print(non_prime)

