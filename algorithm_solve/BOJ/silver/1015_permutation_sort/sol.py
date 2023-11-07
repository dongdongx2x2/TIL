import sys
sys.stdin = open('1015_input.txt')

input = sys.stdin.readline

n = int(input())

lst = list(map(int, input().split()))

sorted_lst = sorted(lst)

ans = [0] * n

for i in range(n):
    idx = sorted_lst.index(lst[i])
    ans[i] = idx
    sorted_lst[idx] = -1

print(*ans)