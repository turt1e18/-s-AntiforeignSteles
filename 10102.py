import sys

count = int(input())
stringList = list(input())

aCount = 0
bCount = 0

for i in range(count):
    if(stringList[i]=="A"):
        aCount += 1
    elif(stringList[i]=="B"):
        bCount += 1

if(aCount > bCount):
    print("A")
elif(aCount < bCount):
    print("B")
elif(aCount == bCount):
    print("Tie")