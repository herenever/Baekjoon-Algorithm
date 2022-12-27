# 문제를 보자마자 순열을 만들어야 겠구나라는 생각이들었고
# 그럼 백트래킹으로 순열을 구현해봐야겠다는 생각이 들었다.

from copy import deepcopy


N = int(input())
numbers = list(map(int,input().split()))
ao = list(map(int,input().split()))
max_val = -1000000001
min_val = 1000000001


def cal(seq):
    global max_val,min_val
    result = numbers[0]
    for i in range(N-1):
        if seq[i] == 0:
            result += numbers[i+1]
        elif seq[i] == 1:
            result -= numbers[i+1]
        elif seq[i] == 2:
            result *= numbers[i+1]
        else:
            if result > 0:
                result //=numbers[i+1]
            else:
                result *= -1
                result //=numbers[i+1]
                result *= -1
    max_val = max(max_val,result)
    min_val = min(min_val,result)

def bt(depth,ao,seq):
    if depth == N-1:
        cal(seq)
        return
    ao = deepcopy(ao)
    for i in range(4):
        if ao[i]:
            ao[i] -= 1
            seq.append(i)
            bt(depth+1,ao,seq)
            ao[i] +=1
            seq.pop()

bt(0,ao,[])
print(max_val)
print(min_val)