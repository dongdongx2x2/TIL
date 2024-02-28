import sys
sys.stdin = open('8980_input.txt')

input = sys.stdin.readline

n, c = map(int, input().split())
m = int(input())
box = []
for _ in range(m):
    s, e, cnt = map(int, input().split())
    box.append((s,e,cnt))

box.sort(key= lambda x: x[1])

village = [c] * (n+1)
ans = 0

for s, e, cnt in box:
    mimi = c

    for i in range(s, e):
        mimi = min(mimi, village[i])
    mimi = min(cnt, mimi)

    for i in range(s, e):
        village[i] -= mimi
    ans += mimi
print(ans)

