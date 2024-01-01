import sys
sys.stdin = open('25644_input.txt')

input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

benefit = 0
ans = 0

for i in range(n-1, -1, -1):
    benefit = max(benefit, lst[i])
    ans = max(ans, benefit - lst[i])

print(ans)