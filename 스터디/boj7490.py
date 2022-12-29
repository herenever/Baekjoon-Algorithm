ao = ["+","-"," "]

def makeEquation(case):
    result = "" 
    for i in range(1,N):
        result += str(i) + ao[case[i-1]]
    result += str(N)
    ans.append(result)

def calculate(case):
    num = [1]
    temp = 0
    sum = 0 
    for i in range(2,N+1):
        if case[i-2] !=2:
            if temp == 0:
                sum += int("".join(map(str,num)))
            else:
                sum -= int("".join(map(str,num)))
            temp = case[i-2]
            num.clear()
        num.append(i)
        
    if temp == 0:
        sum += int("".join(map(str,num)))
    else:
        sum -= int("".join(map(str,num)))   

    if sum == 0:
        return True
    return False

def bt(depth,case):
    if depth == N-1:
        if calculate(case):
            makeEquation(case)
        return
    
    for i in range(3):
        case.append(i)
        bt(depth+1,case)
        case.pop()


T = int(input())
for _ in range(T):
    N = int(input())
    ans = []
    bt(0,[])
    ans.sort()
    for elem in ans:
        print(elem)
    print()