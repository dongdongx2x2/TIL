import sys
sys.stdin = open('17265_input.txt')

input = sys.stdin.readline


def dfs(x, y, value):
    global max_value, min_value

    if x == n - 1 and y == n - 1:
        max_value = max(max_value, value)
        min_value = min(min_value, value)
        return

    for dx, dy in [(0, 1), (1, 0)]:  # 오른쪽과 아래쪽으로만 이동
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n:
            if arr[nx][ny] in ['+', '-', '*']:  # 다음 위치가 연산자인 경우
                if nx + 1 < n:  # 아래로 한 칸 더 이동 가능한 경우
                    next_value = calculate(value, int(arr[nx + 1][ny]), arr[nx][ny])
                    dfs(nx + 1, ny, next_value)
                if ny + 1 < n:  # 오른쪽으로 한 칸 더 이동 가능한 경우
                    next_value = calculate(value, int(arr[nx][ny + 1]), arr[nx][ny])
                    dfs(nx, ny + 1, next_value)
            else:  # 다음 위치가 숫자인 경우
                dfs(nx, ny, value)


def calculate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    else:  # '*'
        return a * b


n = int(input())
arr = [input().split() for _ in range(n)]

max_value = float('-inf')
min_value = float('inf')

dfs(0, 0, int(arr[0][0]))

print(max_value, min_value)