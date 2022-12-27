from collections import deque
N,M = map(int,input().split())
r,c,d = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]
dx = [0,1,0,-1]
dy = [-1,0,1,0]
visited[r][c] = True
ans = 1
cnt = 0

def move():
    global d
    d = (d+3) % 4

def check(nx,ny):
    if 0<= nx < M and 0<= ny < N:
        return True
    return False

def clean(r,c):
    global ans,cnt
    while True:
        move()
        nx = c + dx[d]
        ny = r + dy[d]
        if check(nx,ny) and not visited[ny][nx] and graph[ny][nx] == 0:
            visited[ny][nx] = True
            ans += 1
            r,c = ny,nx
            cnt = 0
            continue
        else:
            cnt += 1
        if cnt == 4:
            nx = c - dx[d]
            ny = r - dy[d]
            if check(nx,ny) and graph[ny][nx] == 0:
                r,c = ny,nx
                cnt = 0
            else:
                break

clean(r,c)
print(ans)