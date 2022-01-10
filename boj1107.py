import sys
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
crushed = list(sys.stdin.readline().split())

def count(num,target):
    if num>target:
        return num-target
    else: 
        return target-num

ans =sys.maxsize
#if N == 100:
#    print(0)
#else:    
for num in range(1000001):
    temp = str(num)
    flag = True
    for s in temp:
        if s in crushed:
            flag = False
    
    if flag:
        cnt = min(len(temp)+count(num,N),count(100,N))
        if cnt<ans:
            ans = cnt
    else:
        cnt = count(100,N)
        if cnt<ans:
            ans = cnt
print(ans)



