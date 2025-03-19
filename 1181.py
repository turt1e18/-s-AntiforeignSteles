import sys

count = int(sys.stdin.readline().rstrip())
a = []

for i in range(count): a.append(sys.stdin.readline().rstrip())

a = sorted(sorted(list(set(a))), key=len)

for i in a:
    print(i)

# sorted는 사전적으로 정리 가능 길이는 정리가 안됨
# key로 len을 추가
# 그럼 진짜 길이순으로 해서 sorted(사전순) 한 다음 sorted(value, key=len)(길이순)으로 재정렬