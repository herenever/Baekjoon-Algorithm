# 구간 합 구하기 4
import sys

N,M = map(int,sys.stdin.readline().split())
numbers = list(map(int,sys.stdin.readline().split()))
dp = [0]*(N+1)
for i in range(1,N+1):
    dp[i] = dp[i-1] + numbers[i-1]

for _ in range(M):
    i,j = map(int,sys.stdin.readline().split())
    print(dp[j]-dp[i-1])