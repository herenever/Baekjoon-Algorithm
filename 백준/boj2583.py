# 수학적 좌표를 일단 이차원 배열로 표현해야겠다
# 사각형이 차지하는 영역을 1로 초기화해야겠다
# 반복문을 돌면서 값이 0 이고 방문이 안된곳에서는 bfs를 돌려야겠다. 그리고 영역count를 1늘려야겠다.

# M은 세로 N 는 가로
from collections import deque
M,N,K = map(int,input().split())
square = []
graph = [[0]*N for _ in range(M)]
visited = [[False]*N for _ in range(M)]
for _ in range(K):
    sy,sx,ey,ex = map(int,input().split())
    for x in range(sx,ex):
        for y in range(sy,ey):
            graph[x][y] = 1

# 동 서 남 북
dx= [0,0,1,-1]
dy =[1,-1,0,0]

def check(nx,ny):
    if 0<=nx<M and 0<=ny<N:
        return True
    return False

def bfs(x,y):
    visited[x][y] = True
    deq = deque()
    deq.append((x,y))
    cnt = 1
    while deq:
        x,y = deq.popleft()
        graph[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if check(nx,ny) and graph[nx][ny] == 0:
                graph[nx][ny] = 1
                cnt += 1
                deq.append((nx,ny)) 

    return cnt

def find():
    for x in range(M):
        for y in range(N):
            if graph[x][y] == 0 and not visited[x][y]:
                return(x,y)
    return(-1,-1)


def solve():
    ans = []
    cnt = 0
    while True:
        x,y = find()
        if (x,y) == (-1,-1):
            ans.sort()
            print(cnt)
            for elem in ans:
                print(elem,end=' ')
            return
        cnt += 1
        area = bfs(x,y)
        ans.append(area)


solve()