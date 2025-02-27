topList = []
caseCount = int(input())
for i in range(caseCount):
    topSchoolName = ""
    topCount = 0
    schoolCount = int(input())
    for j in range(schoolCount):
        tempList = list(map(str,input().split()))
        if(int(tempList[1]) > int(topCount)):
            topCount = tempList[1]
            topSchoolName = tempList[0]
    topList.append(topSchoolName)
for k in range(caseCount):
    print(topList[k])