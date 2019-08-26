def reverse(x):
  y = x.split()
  return " ".join(y[::-1])

i=input("enter string")
print(reverse(i))