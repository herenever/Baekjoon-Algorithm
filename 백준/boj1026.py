N = int(input())
al = list(map(int,input().split()))
bl = list(map(int,input().split()))
al.sort()
bl.sort(reverse=True)
ans = 0
for a,b in zip(al,bl):
    ans += (a*b)

print(ans)