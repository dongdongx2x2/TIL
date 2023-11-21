import sys
sys.stdin = open('14912_input.txt')

input = sys.stdin.readline

n, m = map(int, input().split())
cnt = 0
for i in range(1, n + 1):
    for j in str(i):
        if int(j) == m:
            cnt += 1

print(cnt)
