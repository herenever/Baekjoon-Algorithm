import heapq
import sys
N = int(input())
heap = []
for _ in range(N):
    x = int(sys.stdin.readline())
    if not x:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap,x)
