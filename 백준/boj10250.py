import sys

def roomNumber(h,w,n):
    if n%h ==0:
        if n//h<10:
            print(f"{h}0{n//h}")
        else:
            print(f"{h}{n//h}")
    else:
        if n//h<9:
            print(f"{n%h}0{n//h +1}")
        else:
            print(f"{n%h}{n//h +1}")


n = int(input())
for _ in range(n):
    H,W,N = tuple(map(int,sys.stdin.readline().split()))
    roomNumber(H,W,N)