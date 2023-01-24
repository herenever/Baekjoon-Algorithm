# 비밀번호 찾기

import sys

memo = dict()
N,M = map(int,sys.stdin.readline().split())
for _ in range(N):
    site,pwd = sys.stdin.readline().split()
    memo[site] = pwd
for _ in range(M):
    site = sys.stdin.readline().rstrip()
    print(memo[site])
