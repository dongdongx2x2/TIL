import sys
sys.stdin = open('16208_input.txt')

input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

lst.sort()

sm = sum(lst)
ans = 0

for i in range(n):
    sm -= lst[i]
    ans += lst[i] * sm
print(ans)