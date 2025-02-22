count = int(input())
result = 0
for i in range(count):
    temp = list(map(int, input().split()))
    tempdata = 0
    # 3개 다 같을 때
    if(temp[0] == temp[1] and temp[1] == temp[2]):
        tempdata = 10000 + temp[0] * 1000
    # 2개만 같을 때
    elif(temp[0] == temp[1] or temp[1] == temp[2] or temp[0] == temp[2]):
        if(temp[0] == temp[1] or temp[0] == temp[2]):
            tempdata = 1000 + temp[0] * 100
        elif(temp[1]== temp[2]):
            tempdata = 1000 + temp[1] * 100
    # 1개만 있으면서 최대수 찾기
    else:
        if(temp[0] > temp[1] and temp[0] > temp[2]):
            tempdata = temp[0] * 100
        elif(temp[0] < temp[1] and temp[1] > temp[2]):
            tempdata = temp[1] * 100
        elif(temp[2] > temp[1] and temp[0] < temp[2]):
            tempdata = temp[2] * 100
    if(tempdata > result):
        result = tempdata
print(result)