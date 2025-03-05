import sys

def sol(list):
    if(list[6] > list[9]):
        list[6] += 1
    else:
        list[9] += 1

numList = list(input())
count = [0,0,0,0,0,0,0,0,0,0]
result = 0

for i in range(len(numList)):
    if(numList[i] == "0"): count[0] += 1
    elif(numList[i] == "1"): count[1] += 1
    elif(numList[i] == "2"): count[2] += 1
    elif(numList[i] == "3"): count[3] += 1
    elif(numList[i] == "4"): count[4] += 1
    elif(numList[i] == "5"): count[5] += 1
    elif(numList[i] == "7"): count[7] += 1
    elif(numList[i] == "8"): count[8] += 1
    elif(numList[i] == "6" or numList[i] == "9"): 
        if(count[6] == count[9]):
            count[6] += 1
        else:
            count[9] += 1

print(max(count))


# 입력
# 숫자

# 출력
# 숫자를 만들기 위해 0-9까지 1세트로 필요한 개수

# 조건
# 6 <-> 9 로 변환해서 가능
# ex. 9999 -> 2세트

# 1. 숫자를 받는다
# 2. 숫자를 한개씩 나열한다
# ==== 반복 시작 ====
# 	3. 입력된 숫자당 1개씩 카운트한다
# ==== 반복 끝 ====

# 4. 6과 9의 숫자를 체크한다
# 	조건 -> 공유할 수 있는지 확인
# 		669669 -> 4개
# 		69969 -> 3개
# 		669 -> 2개
# 		666 -> 2개
# 		69 -> 1개
# 5. 제일 많은 숫자를 출력한다


# 1 + 0 = 1 => 1

# 1 + 1 = 2 => 1

# 0 + 3 = 3 => 2

# 1 + 3 = 4 => 2

# 1 + 4 = 5 => 3

# 2 + 4 = 6 => 3

# 3 + 4 = 7 => 4