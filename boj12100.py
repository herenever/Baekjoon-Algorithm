
from copy import deepcopy


N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]



def simultation(board,direction):
    #1.동 2.서 3.남 4.북
    # 한번 바뀌면 top 위치의 블록은 더이상 점수를 합칠수 없으니깐 top을 그다음으로 넘기던지 아니면 어차피 그자리로 납둬도 될듯? 
    if direction == 1:
        for c in range(N):
            top = N-1
            for r in range(N-2,-1,-1):
                if board[c][r]:
                    if board[c][top] == 0:
                        board[c][top] = board[c][r]
                        board[c][r] = 0
                    elif board[c][top] == board[c][r]:
                        board[c][top] = board[c][top] + board[c][top]
                        board[c][r] = 0
                        top -= 1
                    else:
                        top -= 1
                        temp = board[c][r]
                        board[c][r] = 0
                        board[c][top] = temp
                    # 떠나는 자리는 0으로 만들어줘야하고 새로운 top 자리에 현재 위치 값이 가야하기 때문에 이렇게 했다 근데 내가 고민했던 부분은 비어있지 않을경우 
                    # 새로운 top이 현재 위치를 지키고 있기 때문에 값이 0으로 사라지는 아주 큼지막한 오류를 발생시킨다. 따라서 안전하게 swap 해야 했다.

    elif direction == 2:
        for c in range(N):
            top = 0
            for r in range(1,N):
                if board[c][r]:
                    if board[c][top] == 0:
                        board[c][top] = board[c][r]
                        board[c][r] = 0
                    elif board[c][top] == board[c][r]:
                        board[c][top] = board[c][top] + board[c][top]
                        board[c][r] = 0
                        top += 1
                    else:
                        top += 1
                        temp = board[c][r]
                        board[c][r] = 0
                        board[c][top] = temp
    elif direction == 3:
        for r in range(N):
            top = N-1
            for c in range(N-2,-1,-1):
                if board[c][r]:
                    if board[top][r] == 0:
                        board[top][r] = board[c][r]
                        board[c][r] = 0
                    elif board[top][r] == board[c][r]:
                        board[top][r] = board[top][r] + board[top][r]
                        board[c][r] = 0
                        top -= 1
                    else:
                        top -= 1
                        temp = board[c][r]
                        board[c][r] = 0
                        board[top][r] = temp
    
    else:
        for r in range(N):
            top = 0
            for c in range(1,N):
                if board[c][r]:
                    if board[top][r] == 0:
                        board[top][r] = board[c][r]
                        board[c][r] = 0
                    elif board[top][r] == board[c][r]:
                        board[top][r] = board[top][r] + board[top][r]
                        board[c][r] = 0
                        top += 1
                    else:
                        top += 1
                        temp = board[c][r]
                        board[c][r] = 0
                        board[top][r] = temp


def bt(depth,board):
    global ans
    if depth == 5:
        for c in range(N):
            for r in range(N):
                ans = max(ans,board[c][r])
        return

    for i in range(1,5):
        new_board = deepcopy(board)
        simultation(new_board,i)
        bt(depth+1,new_board)
    
# 5번까지 안해보고도 일정수준에서 더이상 움직이는게 필요없다는
# 가지치기를 하면 더 좋을 것 같은데 그걸 하려면 이전 그래프와 다음 그래프를 비교해야하는데 그 시간이 더걸릴 것만 같은 느낌이다.


ans = 0
bt(0,board)
print(ans)