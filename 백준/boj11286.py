# 절댓값 힙

import heapq,sys

N = int(input())
arr = []
for _ in range(N):
    x = int(sys.stdin.readline().rstrip())

    if x == 0:
        if not arr:
            print(0)
        else:
            print(heapq.heappop(arr)[1])
    else:
        heapq.heappush(arr,(abs(x),x))
