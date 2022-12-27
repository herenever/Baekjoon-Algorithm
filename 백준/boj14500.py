N,M = map(int,input().split())
# N 세로 M 가로
paper = [list(map(int,input().split())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]
# 동 서 남 북
dn = [0,0,1,-1]
dm = [1,-1,0,0]

ans = -1

def dfs(cnt,cal,n,m):
    global ans
    if cnt == 3:
        ans = max(cal,ans)
        return
    else:
        for i in range(4):
            nn = n + dn[i]
            nm = m + dm[i]
            if 0<=nn<N and 0<=nm<M and not visited[nn][nm]:
                cal += paper[nn][nm]
                if cnt == 1:
                    visited[nn][nm] = True
                    dfs(cnt+1,cal,n,m)
                    visited[nn][nm] = False
                visited[nn][nm] = True
                dfs(cnt+1,cal,nn,nm)
                visited[nn][nm] = False


for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(0,paper[i][j],i,j)
        visited[i][j] = False

print(ans)

