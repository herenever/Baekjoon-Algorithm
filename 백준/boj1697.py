import sys
from collections import deque
N,K = tuple(map(int,sys.stdin.readline().split()))
visited = [False]*100001
graph = []
for i in range(100001):
    if i ==0:
        graph.append([1])
    #elif i%2 ==0:
    #    graph.append([i-1,i+1,2*i,i//2])
    else:
        graph.append([i-1,i+1,2*i])


def bfs(graph,start,visited,target):
    deq = deque()
    deq.append((start,0))
    visited[start] = True
    while deq:
        node,num = deq.popleft()
        if node == target:
            return print(num)
        for elem in graph[node]:
            if 0<=elem<=100000 and visited[elem] == False:
                visited[elem] = True
                deq.append((elem,num+1))


bfs(graph,N,visited,K)
