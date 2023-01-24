# 테트로미노
# python3 시간초과 pypy 통과

N,M = map(int,input().split())
paper = [list(map(int,input().split())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]

ans = -1

def check(x,y):
    if x>=0 and x<N and y>=0 and y<M:
        return True
    return False

def bt(depth,x,y,temp):
    global ans 
    if depth == 3:
        ans = max(ans,temp)
        return
    
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if check(nx,ny) and not visited[nx][ny]:
            if depth == 1:
                visited[nx][ny] = True
                bt(depth+1,x,y,temp+paper[nx][ny])
                visited[nx][ny] = False
            visited[nx][ny] = True
            bt(depth+1,nx,ny,temp+paper[nx][ny])
            visited[nx][ny] = False


for i in range(N):
    for j in range(M):
        visited[i][j] = True
        bt(0,i,j,paper[i][j])
        visited[i][j] = False

print(ans)

            

