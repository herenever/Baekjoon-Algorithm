import sys

s = sys.stdin.readline().rstrip()
temp =""
a=[]
for i in range(len(s)):
    if i == len(s)-1:
        temp += s[i]
        a.append(int(temp))
    elif s[i] == "-" or s[i] == "+":
        a.append(int(temp))
        a.append(s[i])
        temp = ""
    else: 
        temp +=s[i]

flag =True
ans = 0
for elem in a:
    if flag and elem =="+":
        flag =True
    elif flag and elem == "-":
        flag =False
    elif not flag and elem =="+":
        flag =False
    elif not flag and elem =="-":
        flag = False
    else:
        if flag:
            ans += elem 
        else:
            ans -=elem
        
print(ans)
