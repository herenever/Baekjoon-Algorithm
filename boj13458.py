N = int(input())
people = list(map(int,input().split()))
B,C = map(int,input().split())

def solve():
    ans = 0
    for p in people:
        if p - B <= 0:
            ans +=1
            continue
        if (p-B)%C:
            ans += (p-B)//C + 2
        else:
            ans += (p-B)//C + 1
    print(ans)

solve()