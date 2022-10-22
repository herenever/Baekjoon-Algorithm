# 일단 체크를 해봐야하는건 2번은 오른쪽 톱니에 영향을주고
# 6번은 왼쪽 톱니에 영향을준다. 
# 그리고 톱니바퀴가 4개밖에 없어서 케이스 나눠서 풀어도 될듯한데
# 만약 톱니가 4개가 아니었어도 풀수 있게끔 할순 없을까?
# 첫번쨰 톱니와 마지막 톱니 그리고 이외톱니에서 회전할때 케이스3가지로
# 나누면 좋을 듯싶다.
from collections import deque

gears = [deque(map(int,input())) for _ in range(4)]
K = int(input())
rotates = [tuple(map(int,input().split())) for _ in range(K)]


def turn(idx,dir):
    # 1이면 시계 -1 이면 반시계
    if dir == 1:
        gears[idx].appendleft(gears[idx].pop())
    if dir == -1:
        gears[idx].append(gears[idx].popleft())

def setting(idx,dir):
    idx -= 1
    tl = [0]*4
    tl[idx] = dir
    if idx == 0:
        for i in range(1,4): 
            if gears[i-1][2] == gears[i][6]:
                break
            else:
                tl[i] = -1*tl[i-1]
    elif idx == 3:
        for i in range(2,-1,-1): 
            if gears[i+1][6] == gears[i][2]:
                break
            else:
                tl[i] = -1*tl[i+1]
    else:
        for i in range(idx+1,4):  
            if gears[i-1][2] == gears[i][6]:
                break
            else:
                tl[i] = -1*tl[i-1]
        for i in range(idx-1,-1,-1): 
            if gears[i+1][6] == gears[i][2]:
                break
            else:
                tl[i] = -1*tl[i+1]
    return tl


def simulation():
    for idx,dir in rotates:
        tl = setting(idx,dir)
        for i in range(4):
            turn(i,tl[i])


def solve():
    simulation()
    ans = 0
    mul = 1
    for gear in gears:
        if gear[0]:
            ans += mul
        mul *= 2
    print(ans)
    

solve()


