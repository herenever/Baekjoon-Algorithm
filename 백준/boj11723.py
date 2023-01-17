# 집합
import sys

M = int(input())
s = set()
for _ in range(M):
    command = sys.stdin.readline().rstrip()
    if command.startswith('add'):
        num = int(command.split()[1])
        s.add(num)
    if command.startswith('remove'):
        num = int(command.split()[1])
        try:
            s.remove(num)
        except:
            continue        
    if command.startswith('check'):
        num = int(command.split()[1])
        if num in s:
            print(1)
        else:
            print(0)
    if command.startswith('toggle'):
        num = int(command.split()[1])
        if num in s:
            s.remove(num)
        else:
            s.add(num)
    if command.startswith('all'):
        s = {i for i in range(1,21)}
    if command.startswith('empty'):
        s.clear()
