# 가장 긴 증가하는 부분수열 (11053)

N = int(input())
arr = list(map(int,input().split()))
dp = [1]*N

for i in range(1,N):
    temp = 0
    for j in range(i):
        if arr[j]<arr[i]:
            temp = max(dp[j],temp)
    dp[i] += temp

print(max(dp))
