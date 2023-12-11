import sys
sys.stdin = open('2011_input.txt')

input = sys.stdin.readline

code = list(map(int, input().rstrip()))

dp = [0] * (len(code) + 1)

if code[0] == 0:
    print(0)
else:
    code = [0] + code

    dp[0] = 1
    dp[1] = 1
    for i in range(2, len(code)):
        ten = code[i-1] * 10 + code[i]
        if code[i] > 0:
            dp[i] += dp[i-1]
        if 10 <= ten <= 26:
            dp[i] += dp[i-2]
    print(dp[-1] % 1000000)

