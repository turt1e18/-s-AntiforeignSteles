import sys

n, k = map(int, sys.stdin.readline().split())
listNum = list(range(2, n + 1))
count = 0
result = 0

while True:
    minNum = int(min(listNum))
    for i in listNum:
        if i % minNum == 0:
            count += 1
            result = i
            listNum.remove(i)
        if count == k:
            break
    if count == k:
            break
    
print(result)