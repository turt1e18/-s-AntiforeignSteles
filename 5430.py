from sys import stdin
from collections import deque

cmdList = int(stdin.readline().rstrip())
result = []
for i in range(cmdList):
    isError = False
    isReverse = False

    cmd = list(stdin.readline().rstrip())
    n = int(stdin.readline().rstrip())
    arr = stdin.readline().strip()

    if n == 0:
        isError = True
    else:
        listArr = list(map(int, arr.strip()[1:-1].split(",")))
        dq = deque(listArr)
        
    for i in cmd:
        if i == "R":
            isReverse = not isReverse
        else:
            if isError : break
            if not dq: 
                isError = True 
                break
            
            if isReverse: dq.pop()
            else: dq.popleft()

    if isError:
        result.append("error")
    else:
        if isReverse: 
            dq.reverse()
        result.append(f"[{','.join(map(str, dq))}]")

print("\n".join(result))

from sys import stdin
from collections import deque

cmdList = int(stdin.readline().rstrip())
result = []

for _ in range(cmdList):
    isError = False
    isReverse = False

    cmd = stdin.readline().rstrip()
    n = int(stdin.readline().rstrip())
    arr = stdin.readline().strip()

    if n == 0:
        dq = deque()
    else:
        listArr = list(map(int, arr.strip()[1:-1].split(",")))
        dq = deque(listArr)

    for c in cmd:
        if c == "R":
            isReverse = not isReverse
        else:
            if not dq:
                isError = True
                break
            if isReverse:
                dq.pop()
            else:
                dq.popleft()

    if isError:
        result.append("error")
    else:
        if isReverse:
            dq.reverse()
        result.append(f"[{','.join(map(str, dq))}]")

print("\n".join(result))
