import sys

a, b = sys.stdin.readline().split()

maxA, maxB = int(a), int(b)
maxResult = 0

# U클리드 호제법
while True:
    if(maxA % maxB == 0): 
        maxResult = maxB
        break
    temp = maxA % maxB 
    maxA = maxB
    maxB = temp

# 최소공배수 = a * b / a와 b의 최소공약수
min = int(a) * int(b) / maxResult

print(maxResult)
print(int(min))