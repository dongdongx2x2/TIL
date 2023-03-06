import sys
sys.stdin = open('2615_input.txt')

input = sys.stdin.readline

def digonal2(x, y): # 오른 아래 대각
    # 1일 떄  확인
    if arr[x][y] == 1:
     # 대각 5개 확인
        if arr[x+1][y+1] == 1 and arr[x+2][y+2] == 1 and arr[x+3][y+3] == 1 and arr[x+4][y+4] == 1 and arr[x+5][y+5] != 1 and arr[x-1][y-1] != 1:
            return 1

    # 2일 떄 오른쪽 다섯개 확인
    elif arr[x][y] == 2:
        # 대각 5개 확인
        if arr[x + 1][y + 1] == 2 and arr[x + 2][y + 2] == 2 and arr[x + 3][y + 3] == 2 and arr[x + 4][y + 4] == 2 and arr[x + 5][y + 5] != 2 and arr[x - 1][y - 1] != 2:
            return 2
    return 0

def digonal(x, y): # 왼쪽 위 대각 확인
    if arr[x][y] == 1:
        if arr[x-1][y+1] == 1 and arr[x-2][y+2] == 1 and arr[x-3][y+3] == 1 and arr[x-4][y+4] == 1 and arr[x-5][y+5] != 1 and arr[x+1][y-1] != 1:
            return 1
    elif arr[x][y] == 2:
        if arr[x-1][y+1] == 2 and arr[x-2][y+2] == 2 and arr[x-3][y+3] == 2 and arr[x-4][y+4] == 2 and arr[x-5][y+5] != 2 and arr[x+1][y-1] != 2:
            return 2

    return 0

def width(x,y): # 가로 확인
    # 1일 떄  확인
    if arr[x][y] == 1:
        if arr[x][y + 1] == 1 and arr[x][y + 2] == 1 and arr[x][y + 3] == 1 and arr[x][y + 4] == 1 and arr[x][y + 5] != 1 and arr[x][y - 1] != 1:
            return 1
    elif arr[x][y] == 2:
        if arr[x][y + 1] == 2 and arr[x][y + 2] == 2 and arr[x][y + 3] == 2 and arr[x][y + 4] == 2 and arr[x][y + 5] != 2 and arr[x][y - 1] != 2:
            return 2
    return 0

def height(x,y): # 세로확인
    if arr[x][y] == 1:
        if arr[x+1][y] == 1 and arr[x+2][y] == 1 and arr[x+3][y] == 1 and arr[x+4][y] == 1 and arr[x+5][y] != 1 and arr[x-1][y] != 1:
            return 1

    elif arr[x][y] == 2:
        if arr[x + 1][y] == 2 and arr[x + 2][y] == 2 and arr[x + 3][y] == 2 and arr[x + 4][y] == 2 and arr[x + 5][y] != 2 and arr[x-1][y] != 2:
            return 2
    return 0



arr = [[0]*21] + [[0]+ list(map(int, input().split())) + [0] for _ in range(19)] + [[0]*21]

# for i in arr:
#     print(i)

# 순회하면서 함수를 일단 다확인 0
# 함수를 만들어야 할듯 시작점 기준으로 오른쪽직선 5개 오른쪽 대각선5개 밑 5개 3번확인
# 6목이 될 경우 확인
result = []
for i in range(1, 16): # 오른아래 대각
    for j in range(1, 16):
        # print(win(i,j), i, j)
        if digonal2(i,j) == 1:
            result.append(1)
            result.append((i,j))
        elif digonal2(i,j) == 2:
            result.append(2)
            result.append((i,j))

for i in range(5, 21): # 왼쪽 위 대각 확인
    for j in range(1, 16):
        if digonal(i,j) == 1:
            result.append(1)
            result.append((i,j))
        elif digonal(i,j) == 2:
            result.append(2)
            result.append((i,j))

for i in range(1, 21): # 가로 확인
    for j in range(1, 16):
        if width(i,j) == 1:
            result.append(1)
            result.append((i,j))
        elif width(i,j) == 2:
            result.append(2)
            result.append((i,j))

for i in range(1, 16): # 세로 확인
    for j in range(1, 21):
        if height(i,j) == 1:
            result.append(1)
            result.append((i,j))
        elif height(i,j) == 2:
            result.append(2)
            result.append((i,j))

if result:
    print(result[0])
    print(*result[-1])
else:
    print(0)



