import sys
sys.stdin = open('2304_input.txt')

input = sys.stdin.readline

N = int(input())

data = [list(map(int, input().split())) for _ in range(N)]

data.sort(key=lambda x:x[0])

maxh = max(data, key=lambda x:x[1])
maxh_idx = data.index(maxh)

result = 0

h = data[0][1]
for i in range(maxh_idx):
    if h < data[i+1][1]:
        result += h * (data[i+1][0]-data[i][0])
        h = data[i+1][1]
    else:
        result += h * (data[i+1][0] - data[i][0])

h = data[-1][1]
for i in range(N-1, maxh_idx, -1):
    if h < data[i-1][1]:
        result += h * (data[i][0]-data[i-1][0])
        h = data[i-1][1]
    else:
        result += h * (data[i][0]-data[i-1][0])
result += maxh[1]
print(result)