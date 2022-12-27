def swap(number,f,s):
    num_list = list(str(number))
    temp = num_list[f]
    num_list[f] = num_list[s]
    num_list[s] =  temp
    
    return int("".join(num_list))

def getIdeal(number):
    result = list(str(number))
    result.sort(reverse=True)
    return int("".join(result))


def bt(depth,number):
    global N,ideal,answer
    if depth == len(str(number)):
        answer = max(answer,number)
        return
    if number == ideal:
        if (N-depth) % 2 ==0:
            answer = number
        else:
            answer = swap(number,len(str(number))-1,len(str(number))-2)
        return

    for f in range(len(str(number))-1):
        for s in range(f+1,len(str(number))):
            temp = swap(number,f,s)
            bt(depth+1,temp)

T = int(input())
for i in range(1,T+1):
    number,N =  tuple(map(int,input().split()))
    ideal, answer = getIdeal(number), 0 
    bt(0,number)
    print(f"#{i} {answer}")
     
