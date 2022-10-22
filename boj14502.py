from collections import deque
from copy import deepcopy
N,M = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
virus = []
dx = [1,-1,0,0]
dy = [0,0,1,-1]

# i는 세로 j 는 가로
for i in range(N):
    for j in range(M):
        if graph[i][j] == 2:
            virus.append((i,j))


def check(nx,ny):
    if 0<= nx < M and 0 <= ny < N:
        return True
    return False


def simulation():
    global ans
    cnt = 0
    gr = deepcopy(graph)
    deq = deque()
    for v in virus:
        deq.append(v)
    while deq:
        vy,vx = deq.popleft()
        for i in range(4):
            if check(vx+dx[i],vy+dy[i]) and gr[vy+dy[i]][vx+dx[i]] == 0:
                gr[vy+dy[i]][vx+dx[i]] = 2
                deq.append((vy+dy[i],vx+dx[i]))

    for i in range(N):
        for j in range(M):
            if gr[i][j] == 0:
                cnt += 1
    
    ans = max(ans,cnt)

def select(depth):
    if depth == 3:
        simulation()
        return
    
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                graph[i][j] = 1
                select(depth+1)
                graph[i][j] = 0

def select_2(sx,sy,stack=[]):
    if len(stack) == 3:
        simulation()
        return
    
    for i in range(sy,N):
        sx = sx if i == sx else 0
        for j in range(sx,M):
            if graph[i][j] == 0:
                stack.append((i,j))
                graph[i][j] = 1 
                select_2(j,i,stack)
                graph[i][j] = 0
                stack.pop()

ans = 0
# select(0)
select_2(0,0)
print(ans)

    
            
            



