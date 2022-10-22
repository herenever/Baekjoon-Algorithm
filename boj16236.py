from collections import deque
N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]
# 북 서 동 남
dx = [-1,0,0,1]
dy = [0,-1,1,0]
shark,eat_cnt,ans= 2,0,0
px,py = 0,0
for x in range(N):
    for y in range(N):
        if graph[x][y] == 9:
            px,py = x,y
            graph[x][y] = 0
            break

def check(nx,ny):
    if 0<=nx<N and 0<=ny<N:
        return True
    return False

def search(x,y):
    ans_deq = []
    deq = deque()
    deq.append((x,y,0))
    visited = [[False]* N for _ in range(N)]
    visited[x][y] = True
    while deq:
        px,py,cnt = deq.popleft()
        for i in range(4):
            nx = px + dx[i]
            ny = py + dy[i]
            if check(nx,ny) and not visited[nx][ny] and graph[nx][ny] <= shark:
                if 0 < graph[nx][ny] < shark:
                    visited[nx][ny] = True
                    ans_deq.append((nx,ny,cnt+1))
                else: # 먹을수는 없지만 갈 수는 있을때
                    visited[nx][ny] = True
                    deq.append((nx,ny,cnt+1))
    
    if not len(ans_deq):
        return (-1,-1,-1)
    ax,ay,acnt= 0,0,0
    for i in range(len(ans_deq)):
        if i == 0:
            ax,ay,acnt = ans_deq[i]
            continue
        if acnt == ans_deq[i][2]:
            tx,ty,_ = ans_deq[i]
            if tx < ax:
                ax,ay = tx,ty
                continue
            elif tx == ax:
                if ty < ay:
                    ax,ay = tx,ty
                    continue
        else:
            break
    return (ax,ay,acnt)


def grow(nx,ny,cnt):
    global px,py,ans,eat_cnt,shark
    px,py = nx,ny
    graph[px][py] = 0
    ans += cnt
    eat_cnt += 1
    if eat_cnt == shark:
        shark += 1
        eat_cnt = 0 

def solve():
    while True:
        nx,ny,cnt = search(px,py)
        if (nx,ny,cnt) == (-1,-1,-1):
            break
        grow(nx,ny,cnt)
    print(ans)

solve()
        

# 처음에 상좌우하로 서치 해서 조건에 맞으면 바로 리턴했는데 그렇게 하면 반례가 생긴다
# ex)
#  0 0 0 0
#  0 9 0 1
#  1 0 0 0
#  0 0 0 0
# 현재 위치에서 (1,3)이 return 되어야 하는데 
# 상좌우하로 bfs 돌리면 (2,0) 이 return 된다
# 따라서 같은 시간만큼 걸리는 애들을 모두 찾아서
# 우선조건에 맞는 애를 찾아서 return 해줘야 풀수있었다.