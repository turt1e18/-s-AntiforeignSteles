caseCount = int(input())
result = []
for i in range(caseCount):
    inputCount = int(input())
    tempList = list(map(int, input().split()))
    temp = 0
    for k in range(len(tempList)):
        temp += tempList[k]
    result.append(temp)
for i in range(caseCount):
    print(result[i])