import sys
sys.stdin = open('2841_input.txt')

input = sys.stdin.readline

n, p = map(int, input().split())
stack = [[] for _ in range(7)]

cnt = 0
for _ in range(n):
    a, b = map(int, input().split())

    while stack[a]:
        if stack[a][-1] > b:
            stack[a].pop()
            cnt += 1
        else:
            break
    if stack[a] and stack[a][-1] == b:
        continue
    stack[a].append(b)
    cnt += 1
print(cnt)

