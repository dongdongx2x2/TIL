import sys
sys.stdin = open('2563_input.txt')

input = sys.stdin.readline

N = int(input())
arr = [[0]*100 for _ in range(100)]

for _ in range(N):
    a, b = map(int,input().split())

    for i in range(b, b+10):
        for j in range(a, a+10):
            arr[i][j] = 1

cnt = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] == 1:
            cnt += 1
print(cnt)
