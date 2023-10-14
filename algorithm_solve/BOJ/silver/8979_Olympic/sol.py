import sys

sys.stdin = open('8979_input.txt')

input = sys.stdin.readline

N, K = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

arr.sort(key=lambda x: (x[1], x[2], x[3]), reverse=True)

index = [arr[i][0] for i in range(N)].index(K)

for i in range(N):
    if arr[index][1:] == arr[i][1:]:
        print(i + 1)
        break
