# 최소비용 구하기 (1916)

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


N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
distance = [INF]*(N+1)

for _ in range(M):
    s,e,c = map(int,input().split())
    graph[s].append((c,e))

start,destination = map(int,input().split())
diijkstra(start)
print(distance[destination])