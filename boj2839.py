n = int(input())

result = list()
for x in range(1001):
    for y in range(1667):
        if 5*x + 3*y == n:
            result.append(x+y)

if result:
    print(min(result))
else:
    print(-1)
