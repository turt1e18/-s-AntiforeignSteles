from sys import stdin, stdout
from collections import deque

n = int(stdin.readline().rstrip())
queue = deque(range(1, n+1))
while len(queue) != 1:
    queue.popleft()
    queue.append(queue[0])
    queue.popleft()

stdout.write(str(queue[0]))

# 1. n까지 받기
# ====반복 -> 길이가 1이 될때까지 ====
	
# 	2. 맨 앞에 부분 버리기
# 	3. 그 뒤에 부분 pop 하고 append 하기

# ==== ㅇㅇ ====
# 4. list 0번째 출력

# 근데 del 썻더니 왠 시간초과?
# deque 사용하자