minor = int(input())
max = int(input())
num = 1
powList = []
sum = 0
while 1:
    if(pow(num,2) >= minor and pow(num,2) <= max):
        powList.append(pow(num,2))
    num += 1
    if(pow(num,2) > max):
        break
if(len(powList) == 0):
    print("-1")
else:
    for i in range(len(powList)):
        sum += powList[i]
    print(sum)
    print(powList[0])

# 입력
# a -> 최소값 엔터
# b -> 최대값

# 출력
# 완전제곱수들의 총합
# 최소 완전 제곱수

# 또는

# -1

# 조건
# a와 b 사이의 완전제곱수들 파악
# 하나도 없는 경우 -1을 출력

# 1. 최소값 2개 입력
# 2. 비교 최소값과 최대값 설정
# ---- 반복시작 ----
# 	3. 1부터 n까지 반복하여 제곱한 수를 저장
# 		조건 a이상이면서 b 이하면 저장
# ---- 반복종료 ----
# 4. 저장된 완전제곱수를 총합 계산 후 출력
# 5. 0번째 인덱스 출력