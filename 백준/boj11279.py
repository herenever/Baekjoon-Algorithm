# 최대 힙
import heapq,sys

N = int(input())
arr = []
for _ in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        if not arr:
            print(0)
        else:
            print(-heapq.heappop(arr))
    else:
        heapq.heappush(arr,-x)

