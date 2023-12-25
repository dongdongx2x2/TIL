import sys
sys.stdin = open('9625_inpu.txt')

input = sys.stdin.readline

K = int(input())
a, b = 0, 1
for i in range(1, K):
    a, b = b, a + b
print(a, b)
