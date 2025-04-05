from sys import stdin

listSize = int(stdin.readline().rstrip())
indexList = list(map(int, stdin.readline().split(" ")))
cmdline = int(stdin.readline().rstrip())

mistake = [0] * (listSize - 1)
for i in range(listSize - 1):
    if indexList[i] > indexList[i+1]:
        mistake[i] = 1

prefix = [0] * listSize
for i in range(1, listSize):
    prefix[i] = prefix[i - 1] + mistake[i - 1]

result = []
for _ in range(cmdline):
    x, y = map(int, stdin.readline().split(" "))
    result.append(str(prefix[y - 1] - prefix[x - 1]))

print("\n".join(result))

# for _ in range(cmdline):
#     x, y = map(int, stdin.readline().split(" "))
#     for i in range(x-1 , y-1):
#         if indexList[i] > indexList[i+1]:
#             count+=1
    # result.append(str(count))

# print("\n".join(result))

# 입력
# 배열 크기
# 배열 입력 (공백으로 구분)
# 케이스 입력
# 시작 인덱스 -> 종료 인덱스 (시작 인덱스는 종료보다 작거나 같다)

# 조건 - 인덱스의 값 기준으로 현재 값보다 다음값이 적으면 카운트 1증가
# -> 타임아웃뜸
# ㅅㅂ?

# O(n*n)이라서 그런데

# 그럼 실수한 구간에 대해서 미리 만들어 놓자
