T = int(input())
for _ in range(T):
    n = int(input())
    closet = dict()
    for _ in range(n):
        value,key = input().split()
        if key not in closet:
            closet[key] = [value]
        else:
            closet[key].append(value)
    if len(closet.keys()) == 1:
        print(len(list(closet.values())[0]))
    else:
        temp = 1
        for value in closet.values():
            temp *= (len(value)+1)
        print(temp-1)