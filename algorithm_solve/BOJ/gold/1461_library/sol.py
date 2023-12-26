import sys

sys.stdin = open("1461_input.txt")

input = sys.stdin.readline

N, M = map(int, input().split())
lst = list(map(int, input().split()))

plus  = []
minus  = []
mx = 0
for i in lst:
    mx = max(abs(i), mx)
    if i > 0:
        plus.append(i)
    else:
        minus.append(abs(i))

plus.sort(reverse=True)
minus.sort(reverse=True)

ans = 0

for i in range(0, len(plus), M):
    ans += plus[i] * 2

for i in range(0, len(minus), M):
    ans += minus[i] * 2
ans = ans - mx

print(ans)
