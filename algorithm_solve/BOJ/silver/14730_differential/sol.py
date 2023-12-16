import sys

sys.stdin = open('14730_input.txt')

input = sys.stdin.readline

n = int(input())
ans = 0
for i in range(n):
    c, k = map(int, input().split())
    ans += c * k
print(ans)
