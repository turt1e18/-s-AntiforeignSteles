from sys import stdin

input = stdin.readline
n = int(input().rstrip())

for i in range(1,n+1):
    min_add = list(map(int,str(i)))
    result = i + sum(min_add)
    if n == result:
        print(i)
        break
    if n == i:
        print(0)
        break


# 분해합 = 생성자의 각 자리수를 더한 것 + 생성자
# 생성자를 알아보는법? -> n 보다 밑에 있는 값들 전체 체크