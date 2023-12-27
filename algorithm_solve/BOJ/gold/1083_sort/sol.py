import sys
sys.stdin = open('1083_input.txt')

input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
s = int(input())

for i in range(n):
    if s <= 0:
        break

    mx = max(lst[i:min(n, i + s + 1)])
    idx = lst.index(mx)

    for j in range(idx, i, -1):
        lst[j], lst[j-1] = lst[j-1], lst[j]

    s -= (idx - i)

print(*lst)