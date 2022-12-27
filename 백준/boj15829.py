import sys
L = int(sys.stdin.readline())
line = sys.stdin.readline().rstrip()
M,r,H = 1234567891,31,0
data = [i for i in "abcdefghijklmnopqrstuvwxyz"]

for i in range(L):
    H += (data.index(line[i])+1)*(r**i)

print(H%M)
