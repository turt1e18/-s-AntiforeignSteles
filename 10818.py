import sys

count = int(sys.stdin.readline().rstrip())
num = list(map(int, sys.stdin.readline().split()))
print(min(num), max(num))