import sys
sys.stdin = open('1263_input.txt')

input = sys.stdin.readline

n = int(input())

works = []

for _ in range(n):
    t, s = map(int, input().split())
    works.append((t, s))

works.sort(key=lambda x:x[1])
print(works)

c_time = works[-1][1]

for i in range(n-1, -1, -1):
    t, s = works[i]
    c_time = min(c_time, s) - t

    if c_time < 0:
        print(-1)
        exit()
print(c_time)
