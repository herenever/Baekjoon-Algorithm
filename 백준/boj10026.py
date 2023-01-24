# 적록색약
from collections import deque
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def check(x,y):
    if x>=0 and x<N and y>=0 and y<N:
        return True
    return False

def bfs_True(x,y,color):
    deq = deque()
    deq.append((x,y))
    visited[x][y] = True

    while deq:
        x,y = deq.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if check(nx,ny) and not visited[nx][ny] and graph[nx][ny] == color:
                deq.append((nx,ny))
                visited[nx][ny] = True

def bfs_False(x,y,color):
    deq = deque()
    deq.append((x,y))
    visited[x][y] = True
    if color == 'B':
        while deq:
            x,y = deq.popleft()
            for i in range(4):
                nx,ny = x+dx[i],y+dy[i]
                if check(nx,ny) and not visited[nx][ny] and graph[nx][ny] == color:
                    deq.append((nx,ny))
                    visited[nx][ny] = True
    else:
        while deq:
            x,y = deq.popleft()
            for i in range(4):
                nx,ny = x+dx[i],y+dy[i]
                if check(nx,ny) and not visited[nx][ny]:
                    if graph[nx][ny] != 'B':
                        deq.append((nx,ny))
                        visited[nx][ny] = True



N = int(input())
graph = [list(input()) for _ in range(N)]
visited = [[False]*N for _ in range(N)]


t_ans = 0
f_ans = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs_True(i,j,graph[i][j])
            t_ans +=1

visited = [[False]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs_False(i,j,graph[i][j])
            f_ans +=1

print(t_ans,f_ans)
