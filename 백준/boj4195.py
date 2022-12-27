# child 의 root를 찾는다.
def find(c):
    if c == parent[c]:
        return c
    else:
        root = find(parent[c])
        parent[c] = root
        return parent[c]

def union(x,y):
    root_x = find(x)
    root_y = find(y)

    # 만약 x 와 y 가 한 그룹이 아니었다면
    # y의 root 가 x 의 root의 자식이 되도록하고
    # y 의 root의 집합의 수를 x의 root 집합의 수에 더하도록 한다.
    if root_x != root_y:
        parent[root_y] = root_x
        num[root_x] += num[root_y]


N = int(input())
for _ in range(N):
    F = int(input())
    parent = dict()
    num = dict()
    for _ in range(F):
        x,y = input().split()
        
        if x not in parent:
            parent[x] = x
            num[x] = 1
        if y not in parent:
            parent[y] = y
            num[y] = 1

        union(x,y)
        print(num[find(x)])



