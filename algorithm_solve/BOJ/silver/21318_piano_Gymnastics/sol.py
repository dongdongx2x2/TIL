import sys
sys.stdin = open('21318_input.txt')

input = sys.stdin.readline

N = int(input())
lst = list(map(int,input().split()))
# lst.append(int(1e9)+1)
Q = int(input())

sm = [0] * (N+1)
# print(lst)

cnt = 0
for i in range(1,N):
    if lst[i] < lst[i-1]:
        cnt += 1
    sm[i] = cnt
sm[N] = cnt


for _ in range(Q):
    x, y = map(int,input().split())
    print(sm[y-1]-sm[x-1])

