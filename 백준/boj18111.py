import sys
N,M,B = map(int,sys.stdin.readline().split())
land=[]
for _ in range(N):
    a=list(map(int,sys.stdin.readline().split()))
    for elem in a:
        land.append(elem)
land.sort(reverse=True)
time = sys.maxsize
height = 0

def check(land,h,B):
    temp = 0
    for elem in land:
        if elem > h:
            cnt = elem - h
            B += cnt
            temp += 2*cnt
        elif elem < h:
            cnt = h-elem
            B -= cnt
            temp += cnt
    return temp

for h in range(256,-1,-1):
    if sum(land)+B < N*M*h:
        continue
    temp = check(land,h,B)
    if temp < time :
        time = temp
        height = h

print(time,height) 

# python 으로 하면 시간초과나고 pypy 로하면 통과인데 이유를 모르겠다...
# 완탐을 안해보고 풀수 있을까? 이분탐색으로 하면 종료시점에서 값이 안떨어질것 같다..
