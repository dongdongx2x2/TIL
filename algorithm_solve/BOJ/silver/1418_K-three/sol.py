import sys

sys.stdin = open('1418_input.txt')

input = sys.stdin.readline

n = int(input())
m = int(input())

lst = [0 for i in range(n + 1)]

for i in range(2, n + 1):
    if lst[i] == 0:
        for t in range(i, n + 1, i):
            if t % i == 0:
                lst[t] = max(lst[t], i)
answer = 0
for i in lst:
    if i <= m:
        answer += 1
print(answer - 1)
