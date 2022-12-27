N = int(input())
paper = [list(map(int,input().split())) for _ in range(N)]
blue,white = 0,0

def cut(x,y,n):
    global blue,white
    flag = False
    for i in range(x,x+n):
        if flag:
            break
        for j in range(y,y+n):
            if paper[i][j] != paper[x][y]:
                cut(x,y,n//2)
                cut(x+n//2,y,n//2)
                cut(x,y+n//2,n//2)
                cut(x+n//2,y+n//2,n//2)
                flag = True
                break
    if not flag:
        if paper[x][y]:
            blue += 1
        else:
            white +=1
    

cut(0,0,N)
print(white)
print(blue)