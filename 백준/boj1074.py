import sys

N,r,c = tuple(map(int,sys.stdin.readline().split()))

def find(r,c,n):
    if n == 1:
        if r==0 and c == 0:
            return 0
        elif r==0 and c == 1:
            return 1
        elif r == 1 and c == 0:
            return 2
        else:
            return 3
    if r<(2**n)//2 and c<(2**n)//2:
        return find(r,c,n-1)
    elif r<(2**n)//2 and c>=(2**n)//2:
        return find(r,c-((2**n)//2),n-1) + (4**(n-1))
    elif r>=(2**n)//2 and c<(2**n)//2:
        return find(r-((2**n)//2),c,n-1) + 2*(4**(n-1))
    else:
        return find(r-((2**n)//2),c-((2**n)//2),n-1) + 3*(4**(n-1))

print(find(r,c,N))