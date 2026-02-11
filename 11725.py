from sys import stdin
from collections import deque

input = stdin.readline
node = int(input().rstrip())

d = deque([1])
visited = [False] * (node + 1)
tree = [[]for _ in range(node+1)]

for _ in range(node-1):
    a,b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

visited[1] = True
parent = [0] * (node + 1)

while d:
    now = d.popleft()

    for next in tree[now]:
        if not visited[next]:
            visited[next] = True
            parent[next] = now
            d.append(next)

for i in range(2,node+1):
    print(parent[i])