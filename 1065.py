from sys import stdin

input = stdin.readline

n = int(input().rstrip())

count = 0

for i in range(1,n+1):
    num = list(str(i))
    if len(num) > 2:
        if int(num[1])-int(num[0]) == int(num[2])-int(num[1]): count += 1
    else: count += 1

print(count)