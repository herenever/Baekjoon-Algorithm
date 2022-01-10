import sys
from collections import deque

dx =[0,0,-1,1]
dy =[1,-1,0,-0]

#bfs에서는 큐에 넣을 때 방문체크를 해야 중복계산이 안되어서 시간초과를 피할수 있다.
def bfs(graph,x,y):
    global M,N
    deq = deque()
    deq.append((x,y))
    graph[x][y] = 0
    while deq:
        a,b = deq.popleft()
        for i in range(4):
            nx = a+dx[i]
            ny = b+dy[i]
            if nx<0 or ny<0 or nx>M-1 or ny>N-1:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                deq.append((nx,ny))



T = int(sys.stdin.readline())
for _ in range(T):
    M,N,K = tuple(map(int,sys.stdin.readline().split()))
    graph=[[0 for _ in range(N)] for _ in range(M)]
    for _ in range(K):
        x,y = tuple(map(int,sys.stdin.readline().split()))
        graph[x][y] = 1

    cnt =0
    for i in range(M):
        for j in range(N):
            if graph[i][j] == 1:
                bfs(graph,i,j)
                cnt += 1
    print(cnt)
    











