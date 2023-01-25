# RGB거리

N = int(input())
prices = [list(map(int,input().split())) for _ in range(N)]

line1 = [0]*(N+1) # i번째 집에서 R 색깔을 사용하여 색칠할때 현재까지 든 최소 비용
line2 = [0]*(N+1) # i번째 집에서 G 색깔을 사용하여 색칠할때 현재까지 든 최소 비용
line3 = [0]*(N+1) # i번째 집에서 B 색깔을 사용하여 색칠할때 현재까지 든 최소 비용

line1[1] = prices[0][0] 
line2[1] = prices[0][1]
line3[1] = prices[0][2]

for i in range(2,N+1):
    line1[i] = prices[i-1][0] + min(line2[i-1],line3[i-1])
    line2[i] = prices[i-1][1] + min(line1[i-1],line3[i-1])
    line3[i] = prices[i-1][2] + min(line1[i-1],line2[i-1])

print(min(line1[N],line2[N],line3[N]))
