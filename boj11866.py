import sys
N,K = tuple(map(int,sys.stdin.readline().split()))
index = 0
del_list = list()
people = [i for i in range(1,N+1)]
while(people):
    index = (index + (K-1))%len(people)
    del_list.append(people[index])
    del people[index]

print("<",end="")
for i in range(N):
    if i == N-1:
        print(f"{del_list[i]}>")
    else:
        print(f"{del_list[i]}, ",end="")
