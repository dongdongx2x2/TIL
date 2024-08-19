import sys
sys.stdin = open('17425_input.txt')

input = sys.stdin.readline

mxmx = 1000000
f = [0] * (mxmx + 1)
g = [0] * (mxmx + 1)

for i in range(1, mxmx + 1):
    for j in range(i, mxmx + 1, i):
        f[j] += i

for i in range(1, mxmx + 1):
    g[i] = g[i-1] + f[i]

t = int(input())

for _ in range(t):
    n = int(input())
    print(g[n])
