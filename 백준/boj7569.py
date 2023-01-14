from collections import deque
M,N,H = tuple(map(int,input().split()))
graph = [[list(map(int,input().split())) for _ in range(N)] for _ in range(H)]
tomatoes = []
dx = [0,0,0,0,1,-1]
dy = [0,0,-1,1,0,0]
dz = [1,-1,0,0,0,0]


def bfs(tomatoes):
    day = 0
    deq = deque()
    for x,y,z in tomatoes:
        deq.append((x,y,z,day))
    while deq:
        x,y,z,day = deq.popleft()
        for i in range(6):
            nx,ny,nz = x + dx[i], y+ dy[i], z + dz[i]
            if check(nx,ny,nz) and not graph[nz][nx][ny]:
                deq.append((nx,ny,nz,day+1))
                graph[nz][nx][ny] = 1
    
    for z in range(H):
        for x in range(N):
            for y in range(M):
                if graph[z][x][y] == 0:
                    return -1
    return day

def check(x,y,z):
    if x>=0 and x<N and y>=0 and y<M and z>=0 and z<H:
        return True
    return False

for z in range(H):
    for x in range(N):
        for y in range(M):
            if graph[z][x][y] == 1:
                tomatoes.append((x,y,z))

ans = bfs(tomatoes)
print(ans)