# 나무에 대한 정렬이 필요할 것 같다.
# 또한 해당 나무가 죽었는지에 대한 판단을 어떻게 해야할지 고민해봐야한다

from collections import deque 
N,M,K = tuple(map(int,input().split()))
A = [list(map(int,input().split()))for _ in range(N)]
areas = [[5]*N for _ in range(N)]
trees = [[ deque() for _ in range(N)] for _ in range(N)]

for _ in range(M):
    x,y,age = tuple(map(int,input().split()))
    trees[x-1][y-1].append(age)
dead = [[deque()*N for _ in range(N)] for _ in range(N)]

dx = [-1,-1,-1,0,0,+1,+1,+1]
dy = [-1,0,+1,-1,+1,-1,0,+1]

def spring():
    for i in range(N):
        for j in range(N):
            cnt = 0
            for idx, age in enumerate(trees[i][j]):
                if age <= areas[i][j]:
                    trees[i][j][idx] += 1
                    areas[i][j] -= age
                    continue
                dead[i][j].append(age)
                cnt += 1
            for idx in range(cnt):
                trees[i][j].pop()
    # for x,elems in enumerate(trees):
    #     for y,elem in enumerate(elems):
    #         cnt = 0 

            

def summer():
    for i in range(N):
        for j in range(N):
            for tree in dead[i][j]:
                areas[i][j] += tree//2
            dead[i][j].clear()

def falling():
    for i in range(N):
        for j in range(N):
            cnt = 0
            for age in trees[i][j]:
                if age%5 == 0:
                    cnt +=1
            for _ in range(cnt):
                for k in range(8):
                    nx,ny = i+dx[k],j+dy[k]
                    if check(nx,ny):
                        trees[nx][ny].appendleft(1)

def winter():
    for i in range(N):
        for j in range(N):
            areas[i][j] += A[i][j]

def check(x,y):
    if 0<=x<N and 0<=y<N: return True
    return False


def solution():
    for _ in range(K):  
        spring()
        summer()
        falling()
        winter()
    ans = 0
    for elems in trees:
        for elem in elems:
            ans += len(elem)
    print(ans)

solution()

