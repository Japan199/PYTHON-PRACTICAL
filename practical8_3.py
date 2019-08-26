file=open("p8_3.txt","r+")
wordrepeat={}
total = 0
for word in file.read().split():
    if word not in wordrepeat:
        wordrepeat[word] = 1
        total+=1
    else:
        wordrepeat[word] += 1
    print(word)
print (wordrepeat)
print("Total Names = ",total)
file.close();