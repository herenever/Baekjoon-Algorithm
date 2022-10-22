N = int(input())
schedules = [list(map(int,input().split())) for _ in range(N)]
dp = [0]*N
if schedules[0][0]-1 < N:
    dp[schedules[0][0]-1] = schedules[0][1]


for i in range(1,N):
    t,p = schedules[i]
    dp[i] = max(dp[i-1],dp[i])
    if i+t-1 < N:
        dp[i+t-1] = max(dp[i-1] + p,dp[i+t-1])

print(dp[N-1])


# available = [True]*N
# schedules = sorted(schedules,key = lambda x : (-x[2],x[1]))
# ans = 0


# def check(idx,t):
#     if idx+t > N:
#         return False 
#     for i in range(idx,idx+t):
#         if not available[i]:
#             return False
#     return True

# for schedule in schedules:
#     idx,t,p = schedule
#     if check(idx,t):
#         for i in range(idx,idx+t):
#             available[i] = False
#         ans += p

# print(ans)        




