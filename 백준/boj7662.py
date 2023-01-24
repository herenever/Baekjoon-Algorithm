# 이중 우선순위 큐

import heapq,sys

T = int(input())
for _ in range(T):
    k = int(input())
    maxHeap = []
    minHeap = []
    visited = [False]*k
    for i in range(k):
        command,number = sys.stdin.readline().rstrip().split()
        if command == 'I':
            heapq.heappush(maxHeap,(-int(number),i))
            heapq.heappush(minHeap,(int(number),i))
            visited[i] = True
        else:
            if number == "-1":  # minHeap pop
                while minHeap and not visited[minHeap[0][1]]:
                    heapq.heappop(minHeap)
                if minHeap:
                    visited[minHeap[0][1]] = False
                    heapq.heappop(minHeap)

            else: # maxHeap pop
                while maxHeap and not visited[maxHeap[0][1]]:
                    heapq.heappop(maxHeap)
                if maxHeap:
                    visited[maxHeap[0][1]] = False
                    heapq.heappop(maxHeap)
    
    while minHeap and not visited[minHeap[0][1]]:
        heapq.heappop(minHeap)
    while maxHeap and not visited[maxHeap[0][1]]:
        heapq.heappop(maxHeap)
    
    print(f"{-maxHeap[0][0]} {minHeap[0][0]}" if maxHeap and minHeap else 'EMPTY')