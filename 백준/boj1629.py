# 곱셈 (1629)

# mod 연산은 몇번을 반복해도 한번 한 것과 같다
# a mod c = b mod c 라면 a^k mod c = b^k mod c 이다.

A,B,C = map(int,input().split())


def solve(a,b):
    if b == 1:
        return a%C
    else:
        if b%2 == 0:
            return solve(a,b//2)**2%C
        else:
            return solve(a,(b-1)//2)**2*a%C

print(solve(A,B))