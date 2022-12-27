def check(str):
    stack = list()
    for s in str:
        if s =="(":
            stack.append(s)
        else:
            if not stack:
                return False
            stack.pop()
    
    if stack:
        return False
    return True

n = int(input())
for _ in range(n):
    inp = input()
    if check(inp):
        print("YES")
    else:
        print("NO")
          