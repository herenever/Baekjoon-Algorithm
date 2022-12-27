import sys
def push(stack,x):
    stack.append(x)

def pop(stack):
    if stack:
        return print(stack.pop())
    else:
        return print(-1)

def size(stack):
    return print(len(stack))

def empty(stack):
    if stack:
        return print(0)
    else:
        return print(1)

def top(stack):
    if stack:
        return print(stack[-1])
    else:
        return print(-1)


stack = list()
n = int(sys.stdin.readline())
for _ in range(n):
    act = sys.stdin.readline().split()
    if len(act)>1:
        push(stack,int(act[1]))
    else:
        if act[0] == "pop":
            pop(stack)
        elif act[0] == "size":
            size(stack)
        elif act[0] == "empty":
            empty(stack)
        else:
            top(stack)


