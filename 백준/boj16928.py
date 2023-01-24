# 뱀과 사다리 게임
from collections import deque

def calculate(position):
    for x,y in stairs:
        if x == position:
            return y
    
    for x,y in snakes:
        if x == position:
            return y
    
    return position

def bfs():
    visited = [False]*(101)
    deq = deque()
    deq.append((1,0))
    visited[1] = True

    while deq:
        p,cnt = deq.popleft()
        for i in range(6):
            np = p + dx[i]
            np = calculate(np)
            if np == 100:
                return cnt + 1
            if not visited[np] and np < 100:
                deq.append((np,cnt+1))
                visited[np] = True 

stairs = []
snakes = []
dx = [1,2,3,4,5,6]

N,M = map(int,input().split())
for _ in range(N):
    stairs.append(tuple(map(int,input().split())))
for _ in range(M):
    snakes.append(tuple(map(int,input().split())))

ans = bfs()
print(ans)
