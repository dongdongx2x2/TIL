import sys
sys.stdin = open('7983_input.txt')

input = sys.stdin.readline

n = int(input())

tasks = []
for _ in range(n):
    d, t = map(int, input().split())
    tasks.append((d,t))

tasks.sort(key=lambda x:x[1], reverse=True)

cur_time = tasks[0][1]

for d, t in tasks:
    cur_time = min(cur_time, t)
    cur_time -= d
print(cur_time)