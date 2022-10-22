from collections import deque
N = int(input())
K = int(input())
apples = [tuple(map(int,input().split())) for _ in range(K)]
L= int(input())
directions = deque()
for _ in range(L):
    s,dir = input().split()
    s = int(s)
    directions.append((s,dir))

visited = [[False]*N for _ in range(N)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]
dir_num = 100
ans = 0

def move(nx,ny):
    global ans
    dir_num = 100
    snake_len = 1
    deq = deque()
    while check_range(nx,ny) and not visited[ny][nx]:
        deq.append((nx,ny))
        visited[ny][nx] = True
        # 사과가 있는지 체크
        if check_apple(nx,ny):
            snake_len +=1
        # 자취 초기화
        while len(deq) != snake_len:
            a,b = deq.popleft()
            visited[b][a] = False
        # 방향 바꿔야하는지 체크
        if check_dir(ans):
            _,dir = directions.popleft()
            if dir == 'D':
                dir_num += 1
            else:
                dir_num -= 1

        idx = dir_num % 4
        nx += dx[idx]
        ny += dy[idx]
        ans += 1


def check_range(nx,ny):
    if 0<=nx<N and 0<=ny<N:
        return True
    return False

def check_apple(nx,ny):
    for x,y in apples:
        if (nx+1,ny+1) == (y,x):
            apples.remove((x,y))
            return True
    return False

def check_dir(time):
    if directions:
        if directions[0][0] == time:
            return True
    return False

move(0,0)
print(ans)