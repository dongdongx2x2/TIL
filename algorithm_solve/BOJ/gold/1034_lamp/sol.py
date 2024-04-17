import sys
sys.stdin = open('1034_input.txt')

input = sys.stdin.readline

n, m = map(int, input().split())

lamp = [list(map(int, input().rstrip())) for _ in range(n)]

k = int(input())

ans = 0

for i in range(n):
    zero_cnt = lamp[i].count(0)

    if zero_cnt <= k and (k - zero_cnt) % 2 == 0:
        tem = sum(lamp[i] == lamp[j] for j in range(n))
        ans = max(ans, tem)
print(ans)