import sys
N = int(input())
quad = list()
result = ""
for _ in range(N):
    quad.append(list(sys.stdin.readline().rstrip()))

def check(x,y,n):
    temp = quad[x][y]
    for i in range(n):
        for j in range(n):
            if temp != quad[x+i][y+j]:
                return False
    return True

def divide(x,y,n):
    
    global result
    if check(x,y,n):
        result += quad[x][y]
    else:
        result += "("
        for i in range(2):
            for j in range(2):
                divide(x+i*n//2,y+j*n//2,n//2)
        result +=")"
divide(0,0,N)
print(result)