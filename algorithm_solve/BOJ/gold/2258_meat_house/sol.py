import sys
sys.stdin = open('2258_input.txt')

input = sys.stdin.readline

n, m = map(int, input().split())

meat = []
for _ in range(n):
    weight, price = map(int, input().split())
    meat.append((weight, price))

meat.sort(key=lambda x:(x[1],-x[0]))

# print(meat)

ans = float("INF")

w = 0
tem = 0

for i in range(n):
    w += meat[i][0]

    if i >= 1 and meat[i][1] == meat[i-1][1]:
        tem += meat[i][1]
    else:
        tem = 0

    if w >= m:
        ans = min(ans, meat[i][1] + tem)
print(ans if ans != float("INF") else -1)


