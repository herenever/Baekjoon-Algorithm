from collections import deque
N,M,fuel = tuple(map(int,input().split()))
road = [list(map(int,input().split())) for _ in range(N)]
sx,sy = tuple(map(lambda x: int(x)-1,input().split()))
guests = [list(map(lambda x: int(x)-1,input().split())) for _ in range(M)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
# 동서남북


def check(nx,ny):
    if 0<=nx<N and 0<=ny<N and not road[nx][ny]:
        return True
    return False

def isguest(x,y):
    for gx,gy,dx,dy in guests:
        if (x,y) == (gx,gy):
            return (dx,dy)
    return False

def popguest(x,y,adx,ady):
    didx = 0
    for idx,guest in enumerate(guests):
        if guest == [x,y,adx,ady]:
            didx = idx
            break
    del guests[didx]

def search():
    global fuel,sx,sy
    cost = 0
    cnt = 0
    flag = False
    available = []
    visited = [[False]*N for _ in range(N)]
    deq = deque()
    visited[sx][sy] = True
    dest = isguest(sx,sy)
    if dest:
        popguest(sx,sy,*dest)
        return dest
    deq.append((sx,sy,cnt))
    while deq:
        x,y,cnt = deq.popleft()
        if flag and cost != cnt:
            break
        for i in range(4):
            nx,ny = x + dx[i], y + dy[i]
            if check(nx,ny) and not visited[nx][ny]:
                visited[nx][ny] = True
                dest = isguest(nx,ny)
                if dest:
                    flag = True
                    cost = cnt
                    available.append((nx,ny)+dest)
                    continue         
                deq.append((nx,ny,cnt+1))
    if not flag:
        return (-1,-1)
    
   
    adx,ady = -1,-1
    for idx,elem in enumerate(available):
        tx,ty,tdx,tdy = elem
        if idx == 0:
            sx,sy,adx,ady= tx,ty,tdx,tdy
            continue
        if tx < sx :
            sx,sy,adx,ady = tx,ty,tdx,tdy
        elif tx == sx:
            if ty < sy:
                sx,sy,adx,ady = tx,ty,tdx,tdy
    
    if cost+1 > fuel:
        return (-1,-1)
    fuel -= (cost+1)
    popguest(sx,sy,adx,ady)
    return (adx,ady)

def move(adx,ady):
    
    global fuel,sx,sy
    cost = 0
    visited = [[False]*N for _ in range(N)]
    visited[sx][sy] = True
    if (sx,sy) == (adx,ady):
        return True 
    deq = deque()
    deq.append((sx,sy,cost))
    flag = True
    while deq and flag:
        x,y,cost = deq.popleft()
        for i in range(4):
            nx,ny = x + dx[i] , y+dy[i]
            if check(nx,ny) and not visited[nx][ny]:
                visited[nx][ny] = True
                if (nx,ny) == (adx,ady):
                    cost += 1
                    flag = False
                    break
                deq.append((nx,ny,cost+1))
    
    if flag or cost > fuel:
        return False
    fuel += cost
    sx,sy = adx,ady
    return True

def solve():
    while True:
       
        adx,ady = search()
        if (adx,ady) == (-1,-1):
           
            print(-1)
            return 
        if not move(adx,ady):
            print(-1)
            return
        if len(guests) == 0:
            print(fuel)
            return

solve()





