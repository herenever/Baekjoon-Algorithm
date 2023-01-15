# 카잉 달력
# O(MN)에 해결할 수가 없다
# 그렇다면 수학으로 해결해야 할것 같다.
# 최대값은 M과 N의 최소공배수이다.
# 결국 K번째 수라는 것은 M으로 나누었을때 나머지가 x 이고 
# N으로 나누었을때 나머지가 y 인 값이라는거지 
# 근데 문제는 그런 K가 유일할까? 그걸 모르겠네
# 그리고 문제는 또한 이걸 탐색하려면 최악은 거의 MN이고 이건 시간초과 날것이다.

def GCD(x,y):
    if x%y==0:
        return y
    else:
        return GCD(y,x%y)

T = int(input())
for _ in range(T):
    M,N,x,y = map(int,input().split())
    gcd = GCD(max(M,N),min(M,N))
    lcm = (M*N)//gcd
    ans = -1
    for i in range(x,lcm+1,M):
        if (i-x) % M == 0 and (i-y) % N == 0:
            ans = i
            break
    print(ans)