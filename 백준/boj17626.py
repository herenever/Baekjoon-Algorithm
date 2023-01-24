# Four Squares
# 내 코드가 좀 효율이 구데기인것 같다.

import sys

dp = [0]*50001
dp[2] = 2
dp[3] = 3

i = 1
while i**2 < 50000:
    dp[i**2] = 1
    i += 1


for i in range(4,50001):
    if dp[i] == 0:
        temp = sys.maxsize
        for j in range(1,224):
            if j**2 > i:
                break
            temp = min(temp,dp[j**2]+dp[i-j**2])
        dp[i] = temp



n = int(input())
print(dp[n])