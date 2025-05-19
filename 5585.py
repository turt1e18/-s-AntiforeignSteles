from sys import stdin

change = [500 , 100, 50, 10, 5, 1]
input = stdin.readline
count = 0

n = int(input().rstrip())
result = 1000 - n
while (result > 0):
    if(result >= change[0]):
        result -= change[0]
        count += 1
    elif(result >= change[1]):
        result -= change[1]
        count += 1
    elif(result >= change[2]):
        result -= change[2]
        count += 1
    elif(result >= change[3]):
        result -= change[3]
        count += 1
    elif(result >= change[4]):
        result -= change[4]
        count += 1
    elif(result >= change[5]):
        result -= change[5]
        count += 1
print(count)