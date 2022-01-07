import sys
while(True):
    tri = list(map(int,sys.stdin.readline().split()))
    if sum(tri) == 0:
        break
    tri.sort()
    if tri[0]*tri[0] + tri[1]*tri[1] == tri[2]*tri[2]:
        print("right")
    else:
        print("wrong")