from sys import stdin
from collections import deque

input = stdin.readline
n = int(input().rstrip())
landmap = []
maxh = 0
result = 0

dx=[0,0,1,-1]
dy=[1,-1,0,0]

for _ in range(n):
    r = list(map(int,input().split()))
    landmap.append(r)
    local = max(r)
    
    if maxh < local:
        maxh = local

def bfs(sx,sy,h,visited):
    d = deque()
    d.append((sx,sy))
    visited[sy][sx] = True

    while d:
        x, y = d.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[ny][nx] and landmap[ny][nx] > h:
                    visited[ny][nx] = True
                    d.append((nx,ny))

for i in range(0,maxh+1):
    visited = [[False]*n for _ in range(n)]
    count = 0
    
    for y in range(n):
        for x in range(n):
            if landmap[y][x] > i and not visited[y][x]:
                count += 1
                bfs(x,y,i,visited)
    if result < count:
        result = count

print(result)

# 어차피 다 돌아야함 -> 
# 규칙
# n보다 낮은가 -> 무시하고 다음지역 탐색
# 같거나 높나? -> 비짓저팬에 true 하고 그 부분을 시점으로 bfs 시작
