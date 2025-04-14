from sys import stdin

input = stdin.readline

n = int(input().rstrip())

for _ in range(n):
    facto = int(input().rstrip())
    count = 0
    
    while facto >= 5:
        facto //= 5
        count += facto
    print(count)

# 팩토리얼 마지막이 0으로 끝날려면 10이 곱해져야함
# 10의 약수는 2 * 5인데 2의 배수는 많으니 5의 배수로 판단
# 단 5의 배수만 계산하는게 아니라 5의 제곱인 25 125 ... 도 계산해서 전체를 더해야함