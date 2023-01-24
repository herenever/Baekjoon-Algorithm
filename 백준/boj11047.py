# 동전 0

N,K = map(int,input().split())
coins = [int(input()) for _ in range(N)]

answer = 0

for i in range(N-1,-1,-1):
    if coins[i] <= K:
        answer += K//coins[i]
        K = K%coins[i]

print(answer)