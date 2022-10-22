N = int(input())
a = list(map(int,input().split()))
p = [0]*N
for idx,elem in enumerate(a):
    a[idx] = (idx,elem)
a.sort(key = lambda x:x[1])

for i in range(N):
    p[a[i][0]] = i

print(*p)
