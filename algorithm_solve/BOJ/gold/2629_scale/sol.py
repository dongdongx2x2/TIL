import sys
sys.stdin = open('2629_input.txt')

input = sys.stdin.readline

n = int(input())
n_lst = list(map(int, input().split()))
m = int(input())
m_lst = list(map(int, input().split()))

# 갯수, 무게 dp
dp = [[0] * 40001 for _ in range(n+1)]

# 무개 0 그냥 아무것도 안넣는 한가지
dp[0][0] = 1

for i in range(1, n+1):
    for j in range(40001):
        if dp[i-1][j]:
            dp[i][j] = 1
            dp[i][j+n_lst[i-1]] = 1
            dp[i][abs(j-n_lst[i-1])] = 1

for k in range(m):
    if dp[n][m_lst[k]]:
        print('Y', end=' ')
    else:
        print('N', end=' ')