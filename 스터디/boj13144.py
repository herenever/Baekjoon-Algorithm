N = int(input())
arr = list(map(int,input().split()))
visited = [False]*1000001
end,ans = 0,0

for start in range(N):
    while end<N:
        if visited[arr[end]]:
            break
        visited[arr[end]] = True
        end += 1
    ans += (end-start)
    visited[arr[start]] = False

print(ans)
            
