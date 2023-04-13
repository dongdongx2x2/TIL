import sys
sys.stdin = open('1149_input.txt')

input = sys.stdin.readline

N = int(input())
home = [list(map(int, input().split())) for _ in range(N)]
for i in range(1, N):
    home[i][0] += min(home[i-1][1], home[i-1][2])
    home[i][1] += min(home[i-1][2], home[i-1][0])
    home[i][2] += min(home[i-1][0], home[i-1][1])
print(min(home[N-1]))
