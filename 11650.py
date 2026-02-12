from sys import stdin
from collections import deque

input = stdin.readline

dx=[1,-1,0,0]
dy=[0,0,1,-1]

line = int(input().rstrip())
colormap = []

for _ in range(line):
    colormap.append(list(input().rstrip()))

visited = [[False]*line for _ in range(line)]
n = 0
r_visited = [[False]*line for _ in range(line)]
b = 0

def bfs(rx,ry,blind,visited):
    d = deque([(rx,ry)])
    visited[ry][rx] = True
    color = colormap[ry][rx]
    
    while d:
        x,y = d.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= line or ny >= line:
                continue

            if visited[ny][nx]:
                continue
            
            if not blind:
                    if colormap[ny][nx] != color:
                        continue
            else:
                 if color in "RG" and colormap[ny][nx] in "RG":
                    pass
                 elif colormap[ny][nx] != color:
                    continue
            visited[ny][nx] = True
            d.append((nx,ny))

for iy in range(line):
    for ix in range(line):
        if not visited[iy][ix]:
            bfs(ix,iy,False,visited)
            n += 1

for iy in range(line):
    for ix in range(line):
        if not r_visited[iy][ix]:
            bfs(ix,iy,True,r_visited)
            b += 1

print(n, b)