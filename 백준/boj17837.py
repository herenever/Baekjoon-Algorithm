# 일단 아무 생각이 안든다. 구현문제라는 생각이 들고
# 업어가는 것은 음 union find를 저번에 봐서 그런가
# 업힐때마다 부모로 연결해주는것이 좋을 것 같다는 생각이 들었다.
# 근데 이렇게 하면 움직일 말의 업힌 말들이 뭔지를 파악하는데 K만큼 반복문을 돌아야한다. (근데 K가 10개 미만이긴하다.)
# 또한 순서를 바꾸려할때 즉 Union을 하려고 할때 해당말의 말단 자식이 무엇인지 알아야한다. ==> 이게 얼마나 시간을 많이 잡아먹을지 모르겠다. 구현은 할 수 있을듯 ==> 실패 

# 만약 말 마다 업힌 애들 정보를 가지고 있다면 말이 움직일때마다 해당 정보에 있는 친구들을 초기화 시켜주면 된다. (근데 생각해보니 말갯수가 작아서 별로 안걸릴듯)
# 업힌거는 슬라이싱해주면 될듯

"""
 그래프에서 0은 흰색 1은 빨간색 2는 파란색
 움직이려는 다음칸이 
 0이면 그냥 가면 되고
 1이면 움직인 친구들이 순서가 반대로 해서 쌓아야하고
 2이면 움직이는 방향을 반대로하고 한칸 이동하면 되는데 또 못움직이면
 이동하지않고 방향만 바꾸면 되고 업고있는 친구들도 모두 방향을 바꿔야하는지 모르겠네

"""

N,K = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
state = [ [[] for _ in range(N)] for _ in range(N) ]
pieces = [list(map(lambda x:int(x)-1,input().split())) for _ in range(K)]


dx = [0,0,-1,1]
dy = [1,-1,0,0]


for idx,piece in enumerate(pieces):
    x,y,_ = piece
    state[x][y].append(idx)

def check_range(nx,ny):
    if 0<=nx<N and 0<=ny<N:
        return True
    return False

def find_position(x,y,idx):
    for i,elem in enumerate(state[x][y]):
        if elem == idx:
            return i
    return 

def arrange(x,y,nx,ny,pos):
    temp = state[x][y][pos:]
    for i in temp:
        pieces[i][0],pieces[i][1] = nx,ny

def move(idx):
    x,y,dir = pieces[idx]
    pos = find_position(x,y,idx)
    nx,ny = x+dx[dir],y+dy[dir]
    if check_range(nx,ny):
        if graph[nx][ny] == 0:
            arrange(x,y,nx,ny,pos)
            state[nx][ny] += state[x][y][pos:]
            state[x][y][pos:] = []
        elif graph[nx][ny] == 1:
            arrange(x,y,nx,ny,pos)
            temp = state[x][y][pos:]
            state[nx][ny] += temp[::-1]
            # state[nx][ny] += state[x][y][:pos:-1]
            state[x][y][pos:] = []
        else:
            if dir == 0 or dir == 2:
                dir +=1
            else:
                dir -= 1
            nx,ny,pieces[idx][2] = x+dx[dir],y+dy[dir],dir
            if check_range(nx,ny) and graph[nx][ny] != 2:
                if graph[nx][ny] == 0:
                    arrange(x,y,nx,ny,pos)
                    state[nx][ny] += state[x][y][pos:]
                    state[x][y][pos:] = []
                elif graph[nx][ny] == 1:
                    arrange(x,y,nx,ny,pos)
                    temp = state[x][y][pos:]
                    state[nx][ny] += temp[::-1]
                    # state[nx][ny] += state[x][y][:pos-1:-1]
                    state[x][y][pos:] = []
            else:
                nx,ny = x,y
    else:
        if dir == 0 or dir == 2:
            dir +=1
        else:
            dir -= 1
        nx,ny,pieces[idx][2] = x+dx[dir],y+dy[dir],dir
        if check_range(nx,ny) and graph[nx][ny] != 2:
            if graph[nx][ny] == 0:
                arrange(x,y,nx,ny,pos)
                state[nx][ny] += state[x][y][pos:]
                state[x][y][pos:] = []
            elif graph[nx][ny] == 1:
                arrange(x,y,nx,ny,pos)
                temp = state[x][y][pos:]
                state[nx][ny] += temp[::-1]
                # state[nx][ny] += state[x][y][:pos-1:-1]
                state[x][y][pos:] = []
        else:
            nx,ny = x,y

    if len(state[nx][ny]) >= 4:
        return True
    return False

def solve():
    cnt = 0
    flag = True
    while flag:
        cnt+=1
        if cnt>1000:
            cnt = -1
            flag = False
            break
        else:
            for i in range(K):
                if move(i):
                    flag = False
                    break
    print(cnt)

solve()

# N,K = map(int,input().split())
# dx = [0,0,-1,1]
# dy = [1,-1,0,0]
# graph = [list(map(int,input().split())) for _ in range(N)]
# pieces = [list(map(int,input().split())) for _ in range(K)]
# p_info  = dict()
# for i in range(K):
#     p_info[i] = i

# def check_range(nx,ny):
#     if 0<=nx<N and 0<=ny<N:
#         return True
#     return False

# def find_parent(p,c,path:list):
#     if p_info[c] == c:
#         return []
#     if p_info[c] != p:
#         path.append(c)
#         return find_parent(p,p_info[c],path)
#     path.append(c)
#     return path

# def check_pieces(nx,ny):
#     pass

# def union(p,c):
#     p_info[c] = p


# def move(idx):
#     x,y,dir = pieces[i]
#     path = []
#     for i in range(K):
#         if i == idx:
#             continue
#         temp = find_parent(idx,i,[])
#         if path:
#             if len(path)<len(temp):
#                 path = temp
#     # 여기서 찾은 말단 부터 root 까지는 역순임
#     nx,ny = x + dx[dir] , y + dy[dir]
#     if check_range(nx,ny):
#         if graph[nx][ny] == 0:
#             if 
#         elif graph[nx][ny] == 1:
#             pass
#         else:
#             pass
#     else:
#         pass




        

