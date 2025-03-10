count = int(input())
result = []

for i in range(count):
    result.append(int(input()))

result = sorted(result)

for i in range(len(result)): print(result[i])

# 브2 무지성 코딩