import sys,math
a,b,v = tuple(map(int,sys.stdin.readline().split()))

if a>=v:
    print(1)
else:
    print(math.ceil((v-a)/(a-b))+1)

# 밤에는 절대로 높이만큼 올라갈수 있는것이 아니니깐
# 낮-밤 기준이 아닌 첫날 낮에 올라간 높이를 빼고 
# 밤-낮 을 하루로 잡고 계산해야할 것 같다. 
# 그걸 하루에 올라갈수있는 만큼 나누고 안나누어 떨어지면 하루 더 올라가야되니깐 
# 올림 해주고 첫날을 더해준다.
