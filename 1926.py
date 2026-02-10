from sys import stdin
from collections import deque

input = stdin.readline

n,m = map(int, input().rstrip().split())

dx=[1,-1,0,0]
dy=[0,0,1,-1]
canvas = []
visited = [[False]*m for _ in range(n)]

count = 0
max_area = 0

for _ in range(n):
    canvas.append(list(map(int,input().rstrip().split())))

for y in range(n):

    for x in range(m):

        if canvas[y][x] == 1 and not visited[y][x]:
            count += 1
            d = deque([(x,y)])
            visited[y][x] = True
            area = 1

            while d:
                inx,iny = d.popleft()

                for i in range(4):
                    nx = inx + dx[i]
                    ny = iny + dy[i]    
                    
                    if nx < 0 or ny < 0 or nx >= m or ny >= n:
                        continue
                    if visited[ny][nx] or canvas[ny][nx] == 0:
                        continue
                    
                    visited[ny][nx] = True
                    d.append((nx,ny))
                    area += 1

            max_area = max(max_area, area)
print(count)
print(max_area)