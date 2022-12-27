from collections import deque
n = int(input())
result = list()
for i in range(n):
    age,name = tuple(input().split())
    member = (int(age),name,i)
    result.append(member)

result.sort(key= lambda x:(x[0],x[2]))

for age,name,_ in result:
    print(f"{age} {name}")

