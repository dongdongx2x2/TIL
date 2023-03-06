import sys
sys.stdin = open('3985_input.txt')

input = sys.stdin.readline

L = int(input())
N = int(input())

cake = [0] * (L+1)

mx = 0
for n in range(1, N+1):
    P, K = map(int, input().split())
    for i in range(P, K+1):
        if cake[i] == 0:
            cake[i] = n
    if K-P > mx:
        mx = K-P
        num = n
print(num)

mxmx = 0
for i in range(N):
    if mxmx < cake.count(i+1):
        mxmx = cake.count(i+1)
        a = i+1
print(a)

