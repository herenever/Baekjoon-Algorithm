from collections import deque

N = int(input())
apartments = [list(map(int,input())) for _ in range(N)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(x,y):
    cnt = 1
    deq = deque()
    deq.append((x,y))
    apartments[x][y] = 0
    
    while deq:
        x,y = deq.popleft()
        for i in range(4):
            nx,ny = x + dx[i], y+ dy[i]
            if check(nx,ny) and apartments[nx][ny] == 1:
                deq.append((nx,ny))
                apartments[nx][ny] = 0
                cnt += 1

    return cnt

def check(x,y):
    if x>=0 and x<N and y>=0 and y<N:
        return True
    return False

ans = []
for i in range(N):
    for j in range(N):
        if apartments[i][j] == 1:
            ans.append(bfs(i,j))
ans.sort()
print(len(ans))
for elem in ans:
    print(elem)    

