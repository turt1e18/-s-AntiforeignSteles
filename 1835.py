from sys import stdin
from collections import deque

input = stdin.readline
n = int(input().rstrip())

dq = deque(range(n))
result = [0] * n

for i in range(n):
    temp = 0
    dq.rotate(-(i+1))
    # print(dq, i)
    result[dq.popleft()] = str(i+1)

print(" ".join(result))

# N = 4
# 1X 2X 3X 4X

# 2X 3X 4X 1X 1번셔플
# 1

# 3X 4X 1X

# 1X 3X 4X 2번셔플
# 2

# 3X 4X

# 4X 3X 3번 셔플
# 3

# 3X
# 4

# 1. N 받기
# 0번부터 N번까지 인덱스를 표현하는 리스트 제작 -> deque 넣기
# 결과 리스트 제작
# ==== 반복 ==== -> N번 진행
# 	2. N번 셔플 진행
# 		2-1 -n을 해서 rotate 진행
# 		2-2 맨 앞자리를 pop 해서 진행
# 		2-3 pop 한 값을 정답[pop]에 1부터 기록
# 3. 출력 
