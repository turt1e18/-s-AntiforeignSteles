from sys import stdin
from collections import deque

input = stdin.readline

cmdline = int(input().rstrip())
result = []

for _ in range(cmdline):
    count = 0
    maxValue = 0
    n, m = map(int, input().rstrip().split(" "))
    data = list(enumerate(map(int,input().rstrip().split(" ")))) 
    dq = deque(data)

    while True:
        # print(dq)
        if max(dq, key=lambda x: x[1])[1] == dq[0][1]:
            # print(max(dq, key=lambda x: x[1])[1], dq[0][1])

            temp = dq.popleft()
            count += 1
            if m == temp[0]:
                result.append(str(count))
                break
        else:
            dq.rotate(-1)
    
print(" ".join(result))
    # print(dq[0][0])


#     첫줄
# 테스트 케이스 수량

# 테스크 케이스
# 문서의 개수, 나오는 순서가 궁금한 문서의 인덱스

# 기본 정리



# 1. 입력받을거 다 입력받고
# === 케이스 반복 ===
# 	max = 0 설정
# 	count = 0
# 	=== 케이스 내의 반출 반복 - === -> while(한무)
# 		2. 케이스 내에서 max 값 판별
# 			2-1 맨 앞값이 우선순위가 max 값이라면 pop
# 			2-2 아니라면 rotate 2번 반복
# 				3. 만약 원하던 인덱스의 값이 반출시 케이스 반복으로 break