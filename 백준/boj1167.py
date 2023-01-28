# 트리의 지름 

import sys

def dfs(start,distance,visited):
    global ans,target
    temp = ans
    ans = max(distance,ans)
    if temp != ans:
        target = start

    for node,d in graph[start]:
        if not visited[node]:
            visited[node] = True
            dfs(node,distance+d,visited)

input = sys.stdin.readline
V = int(input())
graph = {i : [] for i in range(1,V+1)}
for _ in range(V):
    info = list(map(int,input().rstrip().rstrip("-1").split()))
    for i in range(1,len(info),2):
        graph[info[0]].append(info[i:i+2])


ans = 0
target = 0
visited = [False]*(V+1)
visited[1] = True
dfs(1,0,visited)

visited = [False]*(V+1)
visited[target] = True
dfs(target,0,visited)



print(ans)