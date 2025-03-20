import sys

while True:
    
    inputList = list(input())
    
    if("".join(inputList) == "0"): break

    reverseNum = list(reversed(inputList))

    if "".join(inputList) == "".join(reverseNum):
        print("yes")
    else:
        print("no")
