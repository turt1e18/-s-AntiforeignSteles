from sys import stdin

input = stdin.readline

a,b = map(int,input().rstrip().split(" "))

print(a+b)

# c라면 정밀도해야하는데 파이썬은 그런거 없다