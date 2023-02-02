# 파티

# dfs를 통한 완전탐색으로 O(2NM)의 시간복잡도를 가질줄 알았다.
# 그러나 생각해보면 하나의 노드에서 dfs를 할 경우
# 최악일때 M보다 더 많이 탐색할 수도 있다. 
# 파티 노드에 닿을때까지 일종의 백트래킹을 하는 것이다.
# 따라서 최악의 경우 시간초과가 날 것을 확인할 수 있다.
# 다익스트라 알고리즘을 통해 각 노드별 최단경로를 작성하고
# 답을 구하는 것이 올바른 풀이이다.

import sys,heapq

def diijstra(start,graph,distance):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist,now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

    
input = sys.stdin.readline
inf = sys.maxsize

N,M,X = map(int,input().split())

graphToParty = [[] for _ in range(N+1)]
graphToHome = [[] for _ in range(N+1)]
distanceToParty = [inf]*(N+1)
distanceToHome = [inf]*(N+1)

for _ in range(M):
    s,d,t = map(int,input().split())
    graphToHome[d].append((s,t))  
    graphToParty[s].append((d,t))

diijstra(X,graphToParty,distanceToParty)
diijstra(X,graphToHome,distanceToHome)




ans = 0
for i in range(1,N+1):
    ans = max(distanceToParty[i]+distanceToHome[i],ans)

print(ans)









# 틀린풀이
# def dfs(start,target,distance,visited):
#     global ans
#     if start == target:
#         ans = min(ans,distance)
#         return
    
#     for node,d in graph[start]:
#         if not visited[node]:
#             visited[node] = True
#             dfs(node,target,distance+d,visited)
#             visited[node] = False


# input = sys.stdin.readline

# N,M,X = map(int,input().split())
# graph = {i : [] for i in range(1,N+1)}

# for _ in range(M):
#     info = list(map(int,input().split()))
#     graph[info[0]].append(info[1:])

# result = []
# for i in range(1,N+1):
    
#     ans = sys.maxsize
#     visited = [False]*(N+1)
#     visited[i] = True
#     dfs(i,X,0,visited)
#     temp = ans
#     ans = sys.maxsize
#     visited = [False]*(N+1)
#     visited[X] = True
#     dfs(X,i,0,visited)
#     temp += ans
#     result.append(temp)   

# print(max(result))
