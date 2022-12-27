T = int(input())
for i in range(1,T+1):
    N,M = tuple(map(int,input().split()))
    wall = [list(map(int,input().split())) for _ in range(N)]

    answer = 0
    for x in range(N-M+1):
        for y in range(N-M+1):
            sum_val = 0
            for n in range(M):
                sum_val += sum(wall[x+n][y:y+M])
            answer = max(sum_val,answer)
    print(f"#{i} {answer}")
