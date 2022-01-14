import sys
N,M = tuple(map(int,sys.stdin.readline().split()))
dic = dict()
arr = [0]*(N+M+1)
cnt = 0
for _ in range(N+M):
    person = sys.stdin.readline().rstrip()
    if dic.get(person) == None:
        dic[person] = cnt
        arr[cnt] +=1
        cnt += 1
    else:
        arr[dic.get(person)] +=1

temp = list(dic.keys())
ans =[]
for i in range(N+M+1):
    if arr[i]>=2:
        ans.append(temp[i])
ans.sort()
print(len(ans))
for elem in ans:
    print(elem)