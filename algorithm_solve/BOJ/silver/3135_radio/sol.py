import sys

sys.stdin = open('3135_input.txt')

input = sys.stdin.readline

a, b = map(int, input().split())
ans = abs(a - b)
for _ in range(int(input())):
    k = int(input())
    if ans > abs(k - b):
        ans = abs(k - b) + 1

print(ans)
