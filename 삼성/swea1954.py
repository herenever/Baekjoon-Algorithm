from collections import deque
T = int(input())
for i in range(1,T+1):
    N = int(input())
    graph = [[0]*N for _ in range(N)]
    # 동 남 서 북
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    num,ridx = 0,0
    deq = deque()
    deq.append((0,0))
    while(deq):
        x,y = deq.popleft()
        num += 1
        graph[x][y] = num
        flag = 0
        while(True):
            if flag == 3:
                break
            nx,ny = x+dx[ridx%4], y+dy[ridx%4]
            if  0<=nx<N and 0<=ny<N and graph[nx][ny] == 0:
                deq.append((nx,ny))
                break
            else:
                ridx += 1
                flag += 1
    print(f"#{i}")
    for elem in graph:
        print(*elem)
        