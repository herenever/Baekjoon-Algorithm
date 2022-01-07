dummy = ["(","[",")","]"]

def push(string,list):
    for elem in string:
        if elem in dummy:
            list.append(elem)
            

def check(list):
    stack = []
    for elem in list:
        if elem in dummy[:2]:
            stack.append(elem)
        elif elem == dummy[2]:
            if stack and stack[-1] == dummy[0]:
                stack.pop()
            else:
                return False
        elif elem == dummy[3]:
            if stack and stack[-1] == dummy[1]:
                stack.pop()
            else:
                return False
    if stack:
        return False
    else:
        return True
                

while(True):
    inp = input()
    if inp == ".":
        break
    bal =list()
    push(inp,bal)
    if check(bal):
        print("yes")
    else:
        print("no")

