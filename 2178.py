from sys import stdin
from collections import deque

input = stdin.readline

n,m = map(int, input().rstrip().split())

# 하상
wayy = [0,0,1,-1]
# 우좌
wayx = [1,-1,0,0]
route = [[0]*m for _ in range(n)]

labyrinth = []
for i in range(n):
    labyrinth.append(list(map(str,input().rstrip())))

d = deque([(0,0)])
route[0][0] = 1

while d:
    x, y = d.popleft()

    for i in range(4):
        nx = x + wayx[i]
        ny = y + wayy[i]

        if nx < 0 or ny >= n or ny< 0 or nx >= m:
            continue
        if labyrinth[ny][nx] == "0":
            continue
        if route[ny][nx] != 0:
            continue

        route[ny][nx] = route[y][x]+1
        d.append((nx,ny))

print(route[n-1][m-1])

# 기본적으로 받고?
# x 또는 y 쪽으로 1 늘어갈때 -> "1" 이면 스택에 넣고 아니면 while 다시 시작해서 pop으로 이전 부분을 얻고
# 최대값 고민하고 최소값 보정하고 벽이면 무시하고 코드 터질부분 커버치고
# 카운트의 조건은? -> bfs 어차피 다 순회하니까 순회한거 거리나타내면 되지않음?
