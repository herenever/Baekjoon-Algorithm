N,d,k,c = tuple(map(int,input().split()))
temp,ans = 1,0
sushi = [int(input()) for _ in range(N)]
visited = [0]*(d+1)
visited[c] = 1

for i in range(k):
    if not visited[sushi[i]]:
        temp += 1
    visited[sushi[i]] += 1
ans = temp
for i in range(N):
    visited[sushi[i%N]] -= 1
    if not visited[sushi[i%N]]:
        temp -= 1
    if not visited[sushi[(i+k)%N]]:
        temp += 1
    visited[sushi[(i+k)%N]] += 1
    ans = max(ans,temp)


print(ans)