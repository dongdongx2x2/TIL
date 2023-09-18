import sys
sys.stdin = open('2217_input.txt')

input = sys.stdin.readline

N = int(input())

weights = []

for _ in range(N):
    w = int(input())
    weights.append(w)

weights.sort(reverse=True)

ans = []

for j in range(N):
    ans.append(weights[j]*(j+1))

print(max(ans))