N,M,H = map(int,input().split())
ladder = [[0 for _ in range(N-1)] for _ in range(H)]
if M:
    for _ in range(M):
        a,b = map(int,input().split())
        ladder[a-1][b-1] = 1
# 가능한 부분 찾고 그거랑 나중에 돌 방문처리할 visited 를 만들어야됨 
available = []



for j in range(H):
    for i in range(N-1):
        if N == 2:
            if not ladder[j][i]:
                available.append((i,j))
        else:
            if i == 0:
                if not ladder[j][i] and not ladder[j][i+1]:
                    available.append((i,j))
            elif i == N-2:
                if not ladder[j][i] and not ladder[j][i-1]:
                    available.append((i,j))
            else:
                if not ladder[j][i] and not ladder[j][i+1] and not ladder[j][i-1]:
                    available.append((i,j))

visited = [False]*len(available)        


# position (i,1) 에서 시작해서 결론은 (i,H) 로 가야한다.
def simulation():
    for i in range(N):
        position = i
        for j in range(H):
            if position == 0:
                if ladder[j][position]:
                    position +=1
            elif position == N-1:
                if ladder[j][position-1]:
                    position -= 1
            else:
                if ladder[j][position]:
                    position += 1 
                elif ladder[j][position-1]:
                    position -= 1
        if position != i:
            return False
    return True

def check(cnt):
    global result
    if cnt > result:
        return 
    if simulation():
        result = cnt
        return 

    # 여기서 시간초과가 나는 것 같은데 
    for idx,elem in enumerate(available):
        if not visited[idx]:
            x,y = elem
            visited[idx] = True
            if not ladder[y][x]:
                ladder[y][x] = 1
                check(cnt+1)
                visited[idx] = False
                ladder[y][x] = 0        

result = 100000
check(0,0)
result =  result if result < 4 else -1
print(result)



    


