import sys
sys.stdin = open('12100_input.txt')

from copy import deepcopy

input = sys.stdin.readline

def left(arr):
    for i in range(n):
        point = 0
        for j in range(1, n):
            if arr[i][j] != 0:
                tem = arr[i][j]
                arr[i][j] = 0

                if arr[i][point] == 0:
                    arr[i][point] = tem
                elif arr[i][point] == tem:
                    arr[i][point] *= 2
                    point += 1
                else:
                    point += 1
                    arr[i][point] = tem
    return arr

def right(arr):
    for i in range(n):
        point = n-1
        for j in range(n-2,-1,-1):
            if arr[i][j] != 0:
                tem = arr[i][j]
                arr[i][j] = 0

                if arr[i][point] == 0:
                    arr[i][point] = tem

                elif arr[i][point] == tem:
                    arr[i][point] *= 2
                    point -= 1

                else:
                    point -= 1
                    arr[i][point] = tem
    return arr

def up(arr):
    for i in range(n):
        point = 0
        for j in range(n):
            if arr[j][i] != 0:
                tem = arr[j][i]
                arr[j][i] = 0

                if arr[point][i] == 0:
                    arr[point][i] = tem

                elif arr[point][i] == tem:
                    arr[point][i] *= 2
                    point += 1

                else:
                    point += 1
                    arr[point][i] = tem
    return arr

def down(arr):
    for i in range(n):
        point = n-1
        for j in range(n-2, -1, -1):
            if arr[j][i] != 0:
                tem = arr[j][i]
                arr[j][i] = 0

                if arr[point][i] == 0:
                    arr[point][i] = tem

                elif arr[point][i] == tem:
                    arr[point][i] *= 2
                    point -= 1

                else:
                    point -= 1
                    arr[point][i] = tem
    return arr

def dfs(arr, depth):
    global mx

    if depth == 5:
        mx = max(mx, max([max(i) for i in arr]))
        return

    for i in range(4):
        copy_arr = deepcopy(arr)

        if i == 0:
            dfs(left(copy_arr), depth + 1)
        elif i == 1:
            dfs(right(copy_arr), depth + 1)
        elif i == 2:
            dfs(up(copy_arr), depth + 1)
        elif i == 3:
            dfs(down(copy_arr), depth + 1)

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

mx = 0
dfs(board, 0)
print(mx)