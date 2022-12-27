# 정렬 알고리즘 구현해서 나중에 풀어보자
import sys

N = int(sys.stdin.readline())
result = [0]*10001
for _ in range(N):
    result[int(sys.stdin.readline())] +=1
cnt = 0

for elem in result:
    if elem ==0:
        cnt +=1
    else:
        for _ in range(elem):
            print(cnt)
        cnt +=1
