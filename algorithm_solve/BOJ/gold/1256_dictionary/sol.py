import sys
sys.stdin = open('1256_input.txt')

input = sys.stdin.readline

def find_dict(n, m, k):
    dp = [[0] * (m+1) for _ in range(n+1)]

    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    if k > dp[n][m]:
        return -1

    result = []
    while n > 0 and m > 0:
        # 'a'를 선택할 경우의 수
        a_count = dp[n - 1][m]

        if k <= a_count:
            result.append('a')
            n -= 1
        else:
            result.append('z')
            m -= 1
            k -= a_count

    # 남은 'a'나 'z' 추가
    result.extend(['a'] * n)
    result.extend(['z'] * m)

    return ''.join(result)
n, m, k = map(int, input().split())

print(find_dict(n,m,k))