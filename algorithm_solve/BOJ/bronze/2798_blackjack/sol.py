import sys
sys.stdin = open('2798_input.txt')

input = sys.stdin.readline

N, M = map(int, input().split())

card = list(map(int, input().split()))

result = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            if card[i]+card[j]+card[k] <= M and result <= card[i]+card[j]+card[k]:
                result = card[i]+card[j]+card[k]
print(result)
