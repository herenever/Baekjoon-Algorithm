# 최단경로 (1753)

import sys,heapq

INF = sys.maxsize
input = sys.stdin.readline

def diijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q:
        dist,now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[0]
            if cost<distance[i[1]]:
                distance[i[1]] = cost
                heapq.heappush(q,(cost,i[1]))

V,E = map(int,input().split())
graph = [[] for _ in range(V+1)]
distance = [INF]*(V+1)
start = int(input())
for _ in range(E):
    u,v,w = map(int,input().split())
    graph[u].append((w,v))

diijkstra(start)

for i in range(1,V+1):
    if distance[i]>= INF:
        print("INF")
    else:
        print(distance[i])