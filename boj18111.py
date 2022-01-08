import sys
N,M,B = map(int,sys.stdin.readline().split())
land=[]
for _ in range(N):
    land.append(list(map(int,sys.stdin.readline().split())))

print(land)