# 역시 그냥 구현문제라는 생각밖에 안든다.
# 좌표 자체를 이차원배열로 만들고 방문처리를 해주고 
# 1*1 짜리 방문처리된것을 카운트 해주면 될 것같은 느낌이든다.
# 문제는 회전시키는 방법인데 그 전세대 까지 꺽은 방향들을 저장해서
# 넘기고 그 방향을 시계 방향으로 90도 전환시킨 정보를 통해서 !!역으로
# 새로운 끝점을 시작점 삼아 그리면 되지 않을까 싶다.
# 90도를 꺽으면 dx 던 dy 던 +1 해주고 나머지 연산해주면 됨

# [0]   이걸보고 0세대 그리고
# [1] 이걸보고 1세대 그리고
# [2,1] 이걸 보고 2세대 그리고
# [2,3,2,1] 이걸 보고 3세대 그리고
# [2,3,0,3,2,3,2,1] 이걸 보고 4세대 그리고

# [[0] [1] [2,1] [2,3,2,1] []]

"""
0 세대는 방향 정보 1개
1 세대는 방향 정보 1개
2 세대는 방향 정보 2개
3 세대는 방향 정보 4개
"""
N = int(input())
dragon_curves = [tuple(map(int,input().split())) for _ in range(N)]
graph = [[0]*101 for _ in range(101)]
dx = [0,-1,0,1]
dy = [1,0,-1,0]

def turn(turns):
    next = []
    dist = len(turns)-1
    for i in range(dist,-1,-1):
        temp = []
        for j in range(len(turns[i])):
            temp.append((turns[i][j]+1)%4)
        next += temp[::-1]
    turns.append(next)
    
def draw(info):
    y,x,dir,gen = info
    turns = [[dir]]
    graph[x][y] = 1
    for i in range(gen+1):
        for d in turns[i]:
            x,y = x+dx[d], y+dy[d]
            graph[x][y] = 1
        turn(turns)

# 주의 해야할점은 x 가 100 이거나 y 가 100일때 graph 에서 1 값이라면 index error 발생하니까 99까지만 돌려줘야댐
def solve():
    for info in dragon_curves:
        draw(info)
    ans = 0
    for x in range(100):
        for y in range(100):
            if graph[x][y]:
                if graph[x+1][y] and graph[x][y+1] and graph[x+1][y+1]:
                    ans +=1
    
    print(ans)


solve()

