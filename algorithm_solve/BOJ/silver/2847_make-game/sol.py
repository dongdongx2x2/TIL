import sys
sys.stdin = open('2847_input.txt')

input = sys.stdin.readline

n = int(input())

lst = []
cnt = 0

for _ in range(n):
    lst.append(int(input()))

for i in range(n - 1, 0, -1):
    if lst[i] <= lst[i - 1]:
        cnt += (lst[i - 1] - lst[i] + 1)
        lst[i - 1] = lst[i] - 1

print(cnt)