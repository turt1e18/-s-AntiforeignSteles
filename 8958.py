import sys

incount = int(input())
resultList = []
for i in range(incount):
    tempList = list(input())
    result = 0
    temp = 1
    # 입력받은 리스트 한번에 훓어보기
    for j in range(len(tempList)):
        # o가 연속인 경우
        # print(j, "re : ",result)
        if(tempList[j] == 'O' and tempList[j] == tempList[j-1] and j >= 1):
            temp = temp + 1
            result = result + temp
            # print("1조건 te :", temp)
        elif(tempList[j] == 'X'):
            temp = 1
            # print("2조건 re :", result)
        elif(tempList[j] == 'O'):
            result = result + 1
            # print("3조건 re :",result)
    resultList.append(result)
for i in range(incount):
    print(resultList[i])

#     입력
# 횟수
# O 또는 X -> 끝나면 엔터 횟수만큼 반복

# 출력
# O 1개당 1점
# X 0점 으로 합산해서 출력

# 조건
# O가 연속적이면 1점식 합산 추가 ex) o -> 1, oo ->12, ooxo -> 1201
# 그러다가 X가 되면 0

# 조건 확률
# oxo
# oox
# xoo


# 1. 횟수 입력받음
# 2. OX 맘대로 입력 
# 3. 계산한 뒤에 리스트에 하나씩 저장
# 4. 다하면 한줄씩 출력