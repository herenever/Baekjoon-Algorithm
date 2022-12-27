def find(x):
    if x == parent[x]:
        return x
    else:
        root = find(parent[x])
        parent[x] = root
        return parent[x]

def union(x,y):
    root_x = find(x)
    root_y = find(y)

    if root_x != root_y:
        parent[root_y] = root_x
        number[root_x] += number[root_y]




N = int(input())
M = int(input())
parent = dict()
number = dict()
for _ in range(M):
    x,y = map(int,input().split())

    if x not in parent:
        parent[x] = x
        number[x] = 1
    if y not in parent:
        parent[y] = y
        number[y] = 1
    
    union(x,y)

print(max(number.values())-1)    