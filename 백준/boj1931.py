import sys
N = int(input())
con = [[0,0] for _ in range(N)]
for i in range(N):
    con[i][0],con[i][1] = tuple(map(int,sys.stdin.readline().split()))

con.sort(key=lambda x:(x[1],x[0]))

cnt = 0
end = 0
for i in range(N):
    if con[i][0] >= end:
        cnt +=1
        end = con[i][1]

print(cnt)
