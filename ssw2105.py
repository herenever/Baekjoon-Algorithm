dx = [-1,1,-1,1] 
dy = [-1,1,1,1]

def check_range(nx,ny):
    if 0<=nx<N and 0<=ny<N: 
        return True
    else:
        False

def check_cafe(nx,ny,vc):
    if cafe[ny][nx] in vc: 
        return False
    else:
        return True

def dfs(idx,sx,sy,nx,ny,vc):
    global ans
    if idx != 0 and nx == sx and ny == sy:
        if idx>ans:
            ans = idx
        return
    for i in range(4):
        nx += dx[i]
        ny += dy[i]
        if check_range(nx,ny):
            if nx == sx and ny == sy:
                dfs(idx+1,sx,sy,nx,ny,vc)
            else:
                if check_cafe(nx,ny,vc) and not visit[ny][nx]:
                    visit[ny][nx] = True
                    vc.append(cafe[ny][nx]) 
                    dfs(idx+1,sx,sy,nx,ny,vc)
                    vc.pop()
                    visit[ny][nx] = False

T = int(input())
for k in range(1,T+1):
    N = int(input())
    cafe = [list(map(int,input().split())) for _ in range(N)]
    visit = [[False]*N for _ in range(N)]
    print(cafe)
    print(visit)
    ans = 0
    vc = []
    for j in range(N):
        for i in range(N):
            print(f"----start {i} {j} ----")
            visit[j][i] = True
            dfs(0,i,j,i,j,vc)
            visit[j][i] = False
    print(f"#{k} {ans}")

