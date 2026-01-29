from sys import stdin

input = stdin.readline

n = int(input().rstrip())
a = list(map(int, input().rstrip().split(" ")))
b = list(map(int, input().rstrip().split(" ")))

a.sort()

result = 0
for i in range(n):
    result += a[i] * max(b)
    b[b.index(max(b))] = -1

print(result)

# a를 정렬 -< 제일 작은게 맨앞
# a[i]부터 b[i]번째중에서 제일 높은애랑 곱해 그리고 그걸 더해 -> 그 요소 삭제, -1로 표기 / n번 반복