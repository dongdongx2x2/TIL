import sys
sys.stdin = open('12892_input.txt')

input = sys.stdin.readline

n, d = map(int, input().split())
gifts = [list(map(int, input().split())) for _ in range(n)]

gifts.sort()

mx = 0
cur = 0
start = 0

for end in range(n):
    cur += gifts[end][1]

    while gifts[end][0] - gifts[start][0] >= d:
        cur -= gifts[start][1]
        start += 1

    mx = max(mx, cur)

print(mx)