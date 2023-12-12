import sys
sys.stdin = open('18428_input.txt')

input = sys.stdin.readline

def back(cnt):
    global flag

    if cnt == 3:
        if bfs():
            flag = True
        return

    for i in range(n):
        for j in range(n):
            if arr[i][j] == "X":
                arr[i][j] = "O"
                back(cnt + 1)
                arr[i][j] = "X"

def bfs():
    for x, y in teacher:
        for dx, dy in ((1, 0),(-1, 0),(0, 1),(0, -1)):
            nx, ny = x, y

            while 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] == "O":
                    break

                if arr[nx][ny] == "S":
                    return False

                nx += dx
                ny += dy
    return True

n = int(input())

arr = [list(input().split()) for _ in range(n)]

teacher = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == "T":
            teacher.append((i, j))
flag = False

back(0)

if flag:
    print("YES")
else:
    print("NO")