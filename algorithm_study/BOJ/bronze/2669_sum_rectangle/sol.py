import sys
sys.stdin = open('2669_input.txt')

input = sys.stdin.readline

arr = [[0]*101 for _ in range(101)]
for i in range(4):
    x1, y1, x2, y2 = map(int, input().split())

    for x in range(x1, x2):
        for y in range(y1, y2):
            arr[x][y] = 1

cnt = 0
for i in arr:
    cnt += sum(i)
print(cnt)