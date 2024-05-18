import sys
sys.stdin = open('1436_input.txt')

n = int(input())
cnt = 0

ans = 666

while 1:
    if '666' in str(ans):
        cnt += 1

    if cnt == n:
        break

    ans += 1

print(ans)