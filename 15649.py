from sys import stdin

input = stdin.readline

n,m = map(int, input().split())
stack = [[]]

while stack:
    path = stack.pop()
    if len(path) == m:
        print(*path)
        continue
    for i in range(n,0,-1):
        if i not in path:
            stack.append(path+[i])