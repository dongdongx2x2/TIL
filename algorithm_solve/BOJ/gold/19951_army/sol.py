import sys
sys.stdin = open('19951_input.txt')

input = sys.stdin.readline

n, m = map(int, input().split())
H = list(map(int, input().split()))

prefix = [0] * (n+1)

for _ in range(m):
    a, b, k = map(int, input().split())

    prefix[a-1] += k
    prefix[b] -= k

for i in range(1, n):
    prefix[i] += prefix[i - 1]

# 최종 높이 계산
for i in range(n):
    H[i] += prefix[i]
print(*H)
