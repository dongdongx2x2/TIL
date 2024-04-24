import sys
sys.stdin = open('2169_input.txt')

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

for j in range(1, m):
    arr[0][j] += arr[0][j-1]

for i in range(1, n):
    LtoR = arr[i][:]
    RtoL = arr[i][:]

    for j in range(m):
        if j == 0:
            LtoR[j] += arr[i-1][j]
        else:
            LtoR[j] += max(arr[i-1][j], LtoR[j-1])

    for j in range(m-1, -1, -1):
        if j == m-1:
            RtoL[j] += arr[i-1][j]
        else:
            RtoL[j] += max(arr[i-1][j], RtoL[j+1])

    for j in range(m):
        arr[i][j] = max(LtoR[j], RtoL[j])

print(arr[n-1][m-1])