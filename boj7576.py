from collections import deque
M,N = map(int,input().split())
tomatos = [list(map(int,input().split())) for _ in range(N)]
x,y = 0,0
ts = []
for i in range(N):
    for j in range(M):
        if tomatos[i][j] == 1:
            ts.append((i,j))
            
            

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(ts):
    day = 0
    deq = deque()
    for x,y in ts:
        deq.append((x,y,day))
    while deq:
        x,y,day = deq.popleft()
        for i in range(4):
            nx,ny = x + dx[i],y+dy[i]
            if 0<=nx<N and 0<=ny<M and tomatos[nx][ny] == 0:
                tomatos[nx][ny] = 1
                deq.append((nx,ny,day+1))
    for i in range(N):
        for j in range(M):
            if tomatos[i][j] == 0:
                print(-1)
                return
    print(day)
    return

bfs(ts)

