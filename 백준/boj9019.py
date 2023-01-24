#DSLR

from collections import deque

commands = ['D','S','L','R']

def calculate(num,command):
    if command == 'D':
        return (2*num)%10000
    if command == 'S':
        if num == 0:
            return 9999
        else:
            return num -1
    if command == 'R':
        return num%10 * 1000 + num//1000 * 100 + num%1000//100 * 10 + num%100//10
    if command == 'L':
        return num%1000//100 * 1000 + num%100//10 * 100 + num%10*10 + num//1000 


def bfs(A,B):
    visited = [False]*10000
    deq = deque()
    deq.append((A,''))
    visited[A] = True

    while deq:
        num,lines = deq.popleft()

        for i in range(4):
            temp = calculate(num,commands[i])
            if temp == B:
                return lines + commands[i]
            if not visited[temp]:
                deq.append((temp,lines+commands[i]))
                visited[temp] = True
                
T = int(input())
for _ in range(T):
    A,B = map(int,input().split())
    ans = bfs(A,B)
    print(ans)


# def bfs(A,B):
#     visited = [False]*10000
#     deq = deque()
#     for i in range(4):
#         deq.append((commands[i],A,commands[i]))
#     visited[A] = True
#     while deq:
#         command,num,lines = deq.popleft()
#         num = calculate(num,command)
#         visited[num] = True

#         if num == B:
#             return lines
        
#         for i in range(4):
#             if not visited[num]:
#                 print(i,lines+commands[i])
#                 deq.append((commands[i],num,lines+commands[i]))