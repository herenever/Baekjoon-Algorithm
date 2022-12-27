import sys
from collections import deque

deq = deque()
n = int(sys.stdin.readline())
for _ in range(n):
    act = sys.stdin.readline().split()
    if len(act)>1:
        if act[0] == "push_back":
            deq.append(act[1])
        else:
            deq.appendleft(act[1])
    else:
        if act[0] == "pop_front":
            if deq:
                print(deq.popleft())
            else:
                print(-1)
        elif act[0] == "pop_back":
            if deq:
                print(deq.pop())
            else:
                print(-1)
        elif act[0] == "size":
            print(len(deq))
        elif act[0] == "empty":
            if deq:
                print(0)
            else: 
                print(1)
        elif act[0] == "front":
            if deq:
                print(deq[0])
            else:
                print(-1)
        else:
            if deq:
                print(deq[-1])
            else:
                print(-1)