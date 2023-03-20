import sys
sys.stdin = open('17299_input.txt')

input = sys.stdin.readline

from collections import Counter

N = int(input())

lst = list(map(int, input().split()))

count = Counter(lst)

stack = []
result = [-1] * N

for i in range(N):
    while stack and stack[-1][1] < count[lst[i]]:
        idx, n = stack.pop()
        result[idx] = lst[i]
    stack.append((i, count[lst[i]]))
print(*result)
