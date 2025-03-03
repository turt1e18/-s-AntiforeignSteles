inputData = []

dataIndex = 0
dataIndexNumber = 0

for i in range(9):
    inputData.append(int(input()))

for j in range(9):
    if(dataIndex < inputData[j]):
        dataIndex = inputData[j]
        dataIndexNumber = j
print(dataIndex)
print(dataIndexNumber + 1)