import sys
N = int(sys.stdin.readline())
cards = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())
find = list(map(int,sys.stdin.readline().split()))
check = [ 0 for _ in range(20000001)]

for elem in cards:
    check[elem+10000000] +=1

for elem in find:
    print(f"{check[elem+10000000]} ",end="")