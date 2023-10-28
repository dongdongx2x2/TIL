import sys
sys.stdin = open('6198_input.txt')

input = sys.stdin.readline

n = int(input())

lst = []
for _ in range(n):
    h = int(input())
    lst.append(h)

cnt = 0
stack = []
for i in range(n):
    while stack and stack[-1] <= lst[i]:
        stack.pop()
    stack.append(lst[i])
    cnt += len(stack) - 1
print(cnt)