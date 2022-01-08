import sys
N,K = tuple(map(int,sys.stdin.readline().split()))
top= 1
bot = 1
for i in range(N,K,-1):
    top *= i
for i in range(1,N-K+1):
    bot *= i

print(top//bot)