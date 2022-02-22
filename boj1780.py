import sys
N = int(sys.stdin.readline())
papers =[]
cnt =[0]*3
for _ in range(N):
    papers.append(list(map(int,sys.stdin.readline().split())))


def isSame(x,y,size):
    temp = papers[x][y]
    for i in range(size):
        for j in range(size):
            if temp != papers[x+i][y+j]:
                return False
    return True

def cut(x,y,size):
    if isSame(x,y,size):
        cnt[papers[x][y]+1] +=1
    else:
        for i in range(3):
            for j in range(3):
                    cut(x+i*size//3,y+j*size//3,size//3)

cut(0,0,N)
print(f"{cnt[0]}\n{cnt[1]}\n{cnt[2]}")
