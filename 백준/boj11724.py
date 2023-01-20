# 연결 요소의 개수
from collections import deque
import sys

def bfs(start,visited,graph):
    deq = deque()
    deq.append(start)
    visited[start] = True

    while deq:
        nn = deq.popleft()
        for node in graph[nn]:
            if not visited[node]:
                deq.append(node)
                visited[node] = True
    


N,M = map(int,input().split())
graph = dict()
for i in range(1,N+1):
    graph[i] = []
visited = [False] * (N+1)
for _ in range(M):
    u,v = map(int,sys.stdin.readline().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)


ans = 0
for node in graph.keys():
    if not visited[node]:
        bfs(node,visited,graph)
        ans += 1

print(ans)