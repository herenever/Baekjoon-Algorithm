from collections import deque
N,M,x,y,K = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
orders  = list(map(int,input().split()))
dice_x = deque([0,0,0,0]) # (n,t,s,b)
dice_y = deque([0,0,0,0]) # (l,t,r,b)
dx = [0,0,0,-1,1]  
dy = [0,1,-1,0,0]

def turn(dir):
    # 동 서 북 남
    if dir == 1:
        dice_y.appendleft(dice_y.pop())
    if dir == 2:
        dice_y.append(dice_y.popleft())
    if dir == 3:
        dice_x.append(dice_x.popleft())
    if dir == 4:
        dice_x.appendleft(dice_x.pop())

def move():
    global x,y
    for order in orders:
        x,y = x+dx[order],y+dy[order]
        if 0<=x<N and 0<=y<M:
            turn(order)
            if order == 1 or order == 2:
                if graph[x][y] == 0:
                    graph[x][y] = dice_y[3]
                else:    
                    dice_y[3] = graph[x][y]
                    graph[x][y] = 0

                dice_x[1],dice_x[3] = dice_y[1],dice_y[3]
                print(dice_y[1])
            if order == 3 or order == 4:
                if graph[x][y] == 0:
                    graph[x][y] = dice_x[3]
                else:
                    dice_x[3] = graph[x][y]
                    graph[x][y] = 0
                dice_y[1],dice_y[3] = dice_x[1],dice_x[3]
                print(dice_x[1])
        else:
            x,y = x-dx[order],y-dy[order]
            continue

move()



