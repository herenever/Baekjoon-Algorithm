from collections import deque
N,M = map(int,input().split())
Map = [list(map(int,input())) for _ in range(N)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def check(nx,ny):
    if 0<=nx<N and 0<=ny<M and Map[nx][ny]:
        return True
    return False


def bfs(x,y):
    visited = [[False]*M for _ in range(N)]
    deq = deque()
    visited[x][y] = True
    deq.append((x,y,1))
    while deq:
        x,y,cnt = deq.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if check(nx,ny) and not visited[nx][ny]:
                visited[nx][ny] = True
                if (nx,ny) == (N-1,M-1):
                    print(cnt+1)
                    return
                deq.append((nx,ny,cnt+1))

bfs(0,0)

