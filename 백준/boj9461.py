# 파도반 수열

T = int(input())
for _ in range(T):
    N = int(input())
    if N>=6:
        dp = [0]*(N+1)
        dp[1] = 1
        dp[2] = 1
        dp[3] = 1
        dp[4] = 2
        dp[5] = 2
        for i in range(6,N+1):
            dp[i] = dp[i-1] + dp[i-5]
    else:
        dp = [0]*6
        dp[1] = 1
        dp[2] = 1
        dp[3] = 1
        dp[4] = 2
        dp[5] = 2
    
    print(dp[N])
