K = int(input())
stack = list()
for _ in range(K):
    n = int(input())
    if n !=0:
        stack.append(n)
    else:
        stack.pop()
print(sum(stack))