import sys
N,M = tuple(map(int,sys.stdin.readline().split()))
doc = dict()
doc_arr = [0]
for i in range(1,N+1):
    name = sys.stdin.readline().rstrip()
    doc_arr.append(name)
    doc[name] = i
for _ in range(M):
    qa = sys.stdin.readline().rstrip()
    if qa.isdigit():
        qa = int(qa)
        print(doc_arr[qa])
    else:
        print(doc[qa])