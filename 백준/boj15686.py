
N,M = map(int,input().split())
city = [list(map(int,input().split())) for _ in range(N)]
chickens = []
houses = []
select_chickens=[]
ans = 10000000

for c in range(N):
    for r in range(N):
        if city[c][r] == 2:
            chickens.append((r,c))
        if city[c][r] == 1:
            houses.append((r,c))

def cal():
    global ans
    result = 0
    for hx,hy in houses:
        temp = 100000
        for cx,cy in select_chickens:
            temp = min(temp,abs(hx-cx)+abs(hy-cy))
        result += temp
    ans = min(ans,result)


# idx = 깊이 , next 치킨집 인덱스
def dfs(idx,next):
    # print(idx,next,select_chickens)
    if idx == M:
        # print("cal")
        cal()
        return
    if next == len(chickens):
        return
    
    dfs(idx,next+1)
    select_chickens.append(chickens[next])
    dfs(idx+1,next+1)
    select_chickens.pop()

    # for i in range(next,len(chickens)):
    #     if chickens[i] in select_chickens:
    #         continue
    #     select_chickens.append(chickens[i])
    #     dfs(idx+1,next+1)
    #     select_chickens.pop()

dfs(0,0)
print(ans)
    






# cases = list(itertools.combinations(chickens,M))

# dx = [1,-1,0,0]
# dy = [0,0,1,-1]

# def check_range(nx,ny):
#     if 0<=nx<N and 0<=ny<N:
#         return True
#     return False

# def make_city(case):
#     new_city = copy.deepcopy(city)
#     for c in range(N):
#         for r in range(N):
#             if city[c][r] == 2:
#                 new_city[c][r] = 0

#     for elem in case:
#         x,y = elem
#         new_city[y][x] = 2

#     return new_city

# def dfs(idx,nx,ny,city):
#     global ans
#     if idx >= ans:
#         return
#     if city[ny][nx] == 2:
#         ans = idx
#         return
#     for i in range(4):
#         if check_range(nx+dx[i],ny+dy[i]) and not visit[ny+dy[i]][nx+dx[i]]:
#             visit[ny+dy[i]][nx+dx[i]] = True
#             dfs(idx+1,nx+dx[i],ny+dy[i],city)
#             visit[ny+dy[i]][nx+dx[i]] = False

# ans = 100000
# result = 100000
# temp = 0

# for case in cases:
#     new_city = make_city(case)
#     ans = 100000
#     for j in range(N):
#         for i in range(N):
#             if new_city[j][i] == 1:
#                 visit[j][i] = True
#                 dfs(0,i,j,new_city)
#                 visit[j][i] = False
#                 temp += ans
#                 ans = 100000
#     if result > temp:
#         result = temp
#     temp = 0

# print(result)

