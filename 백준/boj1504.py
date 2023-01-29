# 특정한 최단 경로


import sys,heapq
input = sys.stdin.readline
INF = sys.maxsize


def diijkstra(start,distance):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q:
        dist,node = heapq.heappop(q)

        if distance[node] < dist:
            continue

        for i in graph[node]:
            cost = dist + i[0]
            if cost<distance[i[1]]:
                distance[i[1]] = cost
                heapq.heappush(q,(cost,i[1]))


N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]
distanceFromOne = [INF]*(N+1)
distanceFromV1 = [INF]*(N+1)
distanceFromV2 = [INF]*(N+1)

for _ in range(M):
    a,b,c = map(int,input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))

v1,v2 = map(int,input().split())

diijkstra(1,distanceFromOne)
diijkstra(v1,distanceFromV1)
diijkstra(v2,distanceFromV2)

ans = min(distanceFromOne[v1]+distanceFromV1[v2]+distanceFromV2[N],distanceFromOne[v2]+distanceFromV2[v1]+distanceFromV1[N])
if ans >= INF:
    print(-1)
else: print(ans)





