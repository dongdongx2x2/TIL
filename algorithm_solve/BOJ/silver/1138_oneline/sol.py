import sys
sys.stdin = open('1138_input.txt')

input = sys.stdin.readline

N = int(input())
lst = list(map(int,input().split()))

ans = [0] * N

for i in range(N):
    tem = 0
    for j in range(N):
        if tem == lst[i] and ans[j] == 0:
            ans[j] = i + 1
            break
        elif ans[j] == 0:
            tem += 1

print(*ans)