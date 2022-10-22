n = int(input())
num = [int(input()) for _ in range(n)]
max_val = max(num)+1
dp = [0]*max_val
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4,max_val):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
for elem in num:
    print(dp[elem])
