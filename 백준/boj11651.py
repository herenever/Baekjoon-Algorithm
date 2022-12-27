import sys

ans= list()
N = int(sys.stdin.readline())
for _ in range(N):
    ans.append(tuple(map(int,sys.stdin.readline().split())))
ans.sort(key= lambda x:(x[1],x[0]))

for elem in ans:
    print(*elem)
