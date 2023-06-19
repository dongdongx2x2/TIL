import sys
sys.stdin = open('2580_input.txt')
input = sys.stdin.readline

def V_Row(x,n):
    for i in range(9):
        if arr[x][i] == n:
            return False
    return True

def V_Col(y,n):
    for i in range(9):
        if arr[i][y] == n:
            return False
    return True

def V_box(x,y,n):
    for i in range(3):
        for j in range(3):
            if arr[x//3 * 3 + i][y//3 * 3 + j] == n: # 3*3 박스
                return False
    return True


def dfs(n):
    if n == len(zero):
        return True
        # for a in arr:
        #     print(*a)
        # exit()

    for i in range(1, 10):
        x = zero[n][0]
        y = zero[n][1]

        if V_Row(x,i) and V_Col(y,i) and V_box(x,y,i):
            arr[x][y] = i
            if dfs(n+1):
                return True
            arr[x][y] = 0
    return False

arr = [list(map(int, input().split())) for _ in range(9)]

zero = []
for i in range(9):
    for j in range(9):
        if not arr[i][j]:
            zero.append([i,j])

dfs(0)

for i in arr:
    print(*i)