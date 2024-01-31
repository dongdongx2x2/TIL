import sys
sys.stdin = open('20207_input.txt')

input = sys.stdin.readline

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]

lst.sort(key=lambda x: (x, -x[1]))

calendar = [0]*366

for s, e in lst:
    for i in range(s, e+1):
        calendar[i] += 1

max_h, w, ans = 0, 0, 0

for i in calendar:
    if i:
        max_h = max(max_h, i)
        w += 1
    else:
        ans += max_h * w
        max_h, w = 0, 0
ans += max_h * w
print(ans)