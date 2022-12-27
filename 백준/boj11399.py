N = int(input())
pi = list(map(int,input().split()))
pi.sort()
for i in range(1,len(pi)):
    pi[i] = pi[i]+pi[i-1]
print(sum(pi))