# 좌표 압축
N = int(input())
dots = list(map(int,input().split()))
result = []
for i in range(N):
    result.append([dots[i],i,-1])

result.sort(key= lambda x:x[0])

temp = result[0][0]
idx = 0
for i in range(N):
    if temp == result[i][0]:
        result[i][2] = idx
    if temp != result[i][0]:
        idx += 1
        temp = result[i][0]
        result[i][2] = idx

result.sort(key= lambda x : x[1])
for i in range(N):
    print(result[i][2], end = " ")
