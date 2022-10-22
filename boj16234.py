from collections import deque
N,L,R = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(x,y,visited):
    deq = deque()
    val = 0
    union = []
    if visited[x][y]:
        return False
    else:
        visited[x][y] = True
        val += graph[x][y]
        union.append((x,y))
        deq.append((x,y))
        while deq:
            x,y = deq.popleft()
            for i in range(4):
                nx,ny = x+dx[i],y+dy[i]
                if 0<=nx<N and 0<=ny<N and not visited[nx][ny] and L<=abs(graph[nx][ny]-graph[x][y])<= R:
                    visited[nx][ny] = True
                    val += graph[nx][ny]
                    union.append((nx,ny))
                    deq.append((nx,ny))
        val //= len(union)
        return (union,val)  



def move(unions,visited):
    for union,val in unions:
        for x,y in union:
            graph[x][y] = val
            visited[x][y] = False

    
def solve():
    visited = [[False]*N for _ in range(N)] 
    day = 0
    while True:
        unions = []
        for i in range(N):
            for j in range(N):
                union = bfs(i,j,visited)
                if union:
                    unions.append(union)
        if len(unions) == N*N:
            print(day)
            return
        move(unions,visited)
        day +=1

solve()