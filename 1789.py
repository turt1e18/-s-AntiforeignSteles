sum = int(input())
n = 0
count = 0

while(True):
    if sum > n:
        n += 1
        sum -= n
        count += 1
    else:
        break
print(n)


# 입력
# 자연수

# 출력
# N의 최대 값

# 조건
# 서로 다른 n개의 자연수 합 = s

# 200 -> 1+?
# 자꾸 20이 나오네 그럼 오버인데
# 그럼 200 에서 -1 씩하는건?
# 200 199 197 194

