import sys

min, max = map(int, sys.stdin.readline().split())

if(min > max):
    temp = max
    max = min
    min = temp

result = []

for i in range(min, max):
    if(min < i and i < max):
        result.append(i)

print(len(result))

for i in result:
    print(i, end=" ")