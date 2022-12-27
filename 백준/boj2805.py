import sys
n,m = tuple(map(int,sys.stdin.readline().split()))
trees = list(map(int,sys.stdin.readline().split()))

def calSum(list,cut):
    sum = 0
    for elem in list:
        if elem > cut:
            sum += elem - cut
    return sum

low = 1
high = 1000000000
mid =0
while(low<=high):
    mid = (low+high)//2
    sum = calSum(trees,mid)
    
    if sum<m:
        high = mid -1
    else:
        low = mid +1


print(high)

    