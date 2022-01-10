import sys
T = int(sys.stdin.readline().rstrip())
one =[0]*41
zero =[0]*41
one[0] = 0
zero[0] = 1
one[1] = 1
zero[1] = 0

for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    for i in range(2,N+1):
        one[i] = one[i-1] + one[i-2]
        zero[i] = zero[i-1] + zero[i-2]
    print(zero[N],one[N])
