import sys
sys.stdin = open('2170_input.txt')

input = sys.stdin.readline

n = int(input())

line = []
for _ in range(n):
    x, y = map(int, input().split())
    line.append((x,y))

line.sort(key=lambda x: x[0])

ans = 0
start = line[0][0]
end = line[0][1]

for i in range(1, n):
    if line[i][0] > end:
        ans += end - start
        start = line[i][0]
        end = line[i][1]
    else:
        end = max(end, line[i][1])

ans += end - start

print(ans)