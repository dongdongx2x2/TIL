import sys
sys.stdin = open('11508_input.txt')

input = sys.stdin.readline

n = int(input())
lst = list(int(input()) for _ in range(n))

lst.sort(reverse=True)

ans = 0

for i in range(n):
    if i % 3 != 2:
        ans += lst[i]

print(ans)