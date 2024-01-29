import sys
sys.stdin = open('10986_input.txt')

input = sys.stdin.readline

n, m = map(int, input().split())
lst = list(map(int, input().split()))

sm = 0
rest = [0] * m

for i in range(n):
    sm += lst[i]
    rest[sm % m] += 1

ans = rest[0]
# print(ans)
for i in range(m):
    ans += rest[i] * (rest[i]-1) // 2

print(ans)