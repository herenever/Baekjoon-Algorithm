import sys
from collections import deque
N,M,V = tuple(map(int,sys.stdin.readline().split()))
graph = [[] for _ in range(N+1)]
for _ in range(M):
    n1,n2 = tuple(map(int,sys.stdin.readline().split()))
    graph[n1].append(n2)
    graph[n2].append(n1)

visited = [False for _ in range(N+1)]

def bfs(graph,start,visited):
    deq = deque()
    deq.append(start)
    visited[start] =True

    while deq:
        n = deq.popleft()
        print(n,end=" ")
        for elem in graph[n]:
            if visited[elem] == True:
                continue
            else:
                visited[elem] = True
                deq.append(elem)

def dfs(graph,start,visited):
    visited[start] = True
    print(start,end=" ")
    graph[start].sort()
    for i in graph[start]:
        if not visited[i]:
            dfs(graph,i,visited) 


dfs(graph,V,visited)
visited = [False for _ in range(N+1)]
print("")
bfs(graph,V,visited)


