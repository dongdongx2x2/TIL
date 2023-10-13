import sys
sys.stdin = open('15684_input.txt')

input = sys.stdin.readline

def check():
    for i in range(N): # 세로선
        now = i
        for j in range(H): # 가로선
            if arr[j][now]:  # 가로선은 고정 세로선 위치 변화
                now += 1
            elif now > 0 and arr[j][now-1]:
                now -= 1
        if now != i:
            return False
    return True


def dfs(x, y, cnt):
    global ans

    if cnt >= ans: # cnt 3이상이거나 ans보다 커지면 그냥 종료
        return
    if check():
        ans = min(cnt, ans)
        return
    if cnt == 3:
        return
    for i in range(x, H):
        k = y if i == x else 0
        for j in range(k, N-1):
            if arr[i][j] == 0:
                arr[i][j] = 1
                dfs(i, j+2, cnt+1)
                arr[i][j] = 0

N, M, H = map(int, input().split())

arr = [[0] * N for _ in range(H)]

for i in range(M):
    a, b = map(int, input().split())
    arr[a-1][b-1] = 1

ans = 4
dfs(0,0,0)


if ans <= 3:
    print(ans)
else:
    print(-1)