import sys
sys.stdin = open('1700_input.txt')

input = sys.stdin.readline

n, k = map(int, input().split())
lst = list(map(int, input().split()))

plug = []
cnt = 0

for i in range(k):
    if lst[i] in plug:
        continue

    if len(plug) < n:
        plug.append(lst[i])
        continue

    priority = []

    for p in plug:
        if p in lst[i:]:
            priority.append(lst[i:].index(p))

        else:
            priority.append(101)

    goal = priority.index(max(priority))
    del plug[goal]
    plug.append(lst[i])
    cnt += 1

print(cnt)