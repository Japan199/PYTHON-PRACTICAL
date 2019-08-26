# generate a password with length "passlen" with no duplicate characters in the password

import random

s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"

n = int(input("Enter allowed number of special characters : "))
print("Enter allowed special characters : ")

for i in range(0, n):
    element = input()
    s += element
print(list)


passlen = int(input("Enter length of password : "))

p =  "".join(random.sample(s,passlen ))
print (p)