import sys
sys.stdin = open('17390_input.txt')

input = sys.stdin.readline

n, q = map(int, input().split())
num = list(map(int, input().split()))
num.sort()

prefix_sum = [0]
for i in range(n):
    prefix_sum.append(prefix_sum[i] + num[i])

for _ in range(q):
    L, R = map(int, input().split())
    print(prefix_sum[R] - prefix_sum[L - 1])
