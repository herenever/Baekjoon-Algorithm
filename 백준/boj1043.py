# 거짓말

from collections import deque

def bfs(start):
    visited = [False]*(N+1)
    deq = deque()
    deq.append(start)
    visited[start] = True

    while deq:
        node = deq.popleft()
        for elem in graph[node]:
            if not visited[elem]:
                truth[elem] = True
                visited[elem] = True
                deq.append(elem)                




N,M = map(int,input().split())
graph = {i : set() for i in range(1,N+1)}
truth = [False]*(N+1)
lines = input()
known = []
parties = []
ans = 0
if not lines.startswith('0'):
    known = list(map(int,lines.split()))[1:]

for _ in range(M):
    party = list(map(int,input().split()))
    size,people = party[0],party[1:]
    parties.append(party)
    for i in range(size):
        for j in range(size):
            if people[i] != people[j]:
                graph[people[i]].add(people[j])

for elem in known:
    truth[elem] = True
    bfs(elem)

for party in parties:
    size,people = party[0],party[1:]
    flag = False
    for i in range(size):
        if truth[people[i]]:
            flag = True
            break
    
    if not flag:
        ans += 1

print(ans)