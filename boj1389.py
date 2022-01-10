import sys
from collections import deque
N,M = map(int,sys.stdin.readline().split())
graph=[[] for _ in range(N+1)]
for _ in range(M):
    n1,n2 = tuple(map(int,sys.stdin.readline().split()))
    graph[n1].append(n2)
    graph[n2].append(n1)

visited = [False]*(N+1)
ans = 0
temp =sys.maxsize

def bfs(graph,start,visited):
    cnt = 0
    result = [0]*(N+1)
    deq = deque()
    deq.append((start,cnt))
    visited[start] = True

    while deq:
        n,num= deq.popleft()
        result[n] = num
        cnt += 1
        for elem in graph[n]:
            if visited[elem]:
                continue
            visited[elem] = True
            deq.append((elem,cnt))
    return sum(result)



for i in range(1,N+1):
    cnt = bfs(graph,i,visited)
    if cnt<temp:
        temp = cnt
        ans = i
    visited = [False]*(N+1)
print(ans)



