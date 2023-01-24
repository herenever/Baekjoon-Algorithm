# 경로 찾기

from copy import deepcopy
from collections import deque

def bfs(start,target):
    visited = [False]*N
    deq = deque()
    deq.append(start)
    if start != target:
        visited[start] = True

    while deq:
        next_node = deq.popleft()
        for i in range(N):
            if graph[next_node][i] and not visited[i]:
                if i == target:
                    return True
                deq.append(i)
                visited[i] = True
    return False


N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]
answer = deepcopy(graph)

for i in range(N):
    for j in range(N):
        if bfs(i,j):
            answer[i][j] = 1

for elem in answer:
    print(*elem)

