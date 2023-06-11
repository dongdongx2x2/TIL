import sys
sys.stdin = open('5525_input.txt')

input = sys.stdin.readline

N = int(input())
M = int(input())
S = input().rstrip()

now, cnt, ans = 0,0,0

while now < (M-1):
    if S[now:now+3] == 'IOI':
        cnt += 1
        now += 2

        if cnt == N:
            ans += 1
            cnt -= 1

    else:
        now += 1
        cnt = 0

print(ans)