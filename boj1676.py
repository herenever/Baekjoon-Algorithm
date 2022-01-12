import sys
N = int(sys.stdin.readline().rstrip())
two = 0
five = 0
for i in range(1,N+1):
    temp = i
    if i % 2 ==0:
        while(temp%2 == 0):
            temp = temp //2
            two +=1
    temp = i
    if i % 5 == 0:
        while(temp%5 == 0):
            temp = temp //5
            five +=1

print(min(two,five))
