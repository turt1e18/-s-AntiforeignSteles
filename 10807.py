inputNumCount = int(input())
list = list(map(int, input().split()))
findNum = int(input())
count = 0
for i in range(inputNumCount):
    if(findNum == list[i]): count += 1
print(count)