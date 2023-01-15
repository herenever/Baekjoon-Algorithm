from collections import deque

def solve(arr,commands):
    stack = []
    cnt = 0
    for command in commands:
        if command == 'D':
            cnt += 1

        if not stack:
            stack.append(command)
        else:
            if stack[-1] == 'R':
                if command == stack[-1]:
                    stack.pop()
                else:
                    stack.append(command)
            else:
                stack.append(command)
    
    if cnt > len(arr):
        return "error"

    flag = True
    for command in stack:
        if command == 'D':
            if flag:
                arr.popleft()
            else:
                arr.pop()
        if command == 'R':
            flag = not flag
    
    if not flag:
        arr.reverse()
    
    return list(arr)


T = int(input())
for _ in range(T):
    p = input()
    n = int(input())
    arr = deque(eval(input()))
    print(str(solve(arr,p)).replace(" ",""))