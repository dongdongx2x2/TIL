import sys
sys.stdin = open('1758_input.txt')

input = sys.stdin.readline

n = int(input().rstrip())
lst = [int(input().rstrip()) for _ in range(n)]

lst = sorted(lst, reverse=True)
ans = 0

for i in range(n):
    tmp = lst[i] - i
    if tmp < 0:
        continue
    ans += tmp

print(ans)
