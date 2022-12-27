def dfs(idx,K,next):
    global ans
    if idx >= ans:
        return
    if check():
        ans = idx
        return
    if idx == K-1:
        ans = K
        return

    for i in range(next,D):
        for d in range(2):
            drug = [d]*W
            temp = film[i]
            film[i] = drug
            dfs(idx+1,K,i+1)
            film[i] = temp


def check():
    test = [False] * W
    cnt = 0
    temp = 100
    for i in range(W):
        for j in range(D):
            if j == 0:
                cnt += 1
                temp = film[j][i]
            else:
                if temp == film[j][i]:
                    cnt +=1
                else:
                    cnt = 1 
                    temp = film[j][i]
            if cnt == K:
                test[i] = True
                cnt = 0
                break
        if not test[i]:
            return False
        cnt = 0

    for elem in test:
        if not elem:
            return False
    
    return True


T = int(input())
for i in range(T):
    D,W,K = map(int,input().split())
    film = [list(map(int,input().split())) for _ in range(D)]
    ans = K+1
    dfs(0,K,0)
    print(i+1,ans)



