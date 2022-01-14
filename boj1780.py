import sys
N = int(sys.stdin.readline())
papers =[]
cnt =[0]*3
for _ in range(N):
    papers.append(list(map(int,sys.stdin.readline().split())))

print(papers[0][0:3])

def isSame(graph):
    size = len(graph)
    temp = graph[0][0]
    for i in range(size):
        for j in range(size):
            if temp != graph[i][j]:
                return False
    return True

def cut(graph):
    size = len(graph)
    if isSame(graph):
        if graph[0][0] == -1:
            cnt[0] += size
        elif graph[0][0] == 0:
            cnt[1] += size
        else:
            cnt[2] += size
    else:
        
        for i in range(size):
            pass