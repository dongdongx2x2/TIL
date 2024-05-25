import sys

sys.stdin = open('7795_input.txt')

input = sys.stdin.readline
import bisect

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))
    cnt = 0
    for i in A:
        cnt += (bisect.bisect(B, i-1))
    print(cnt)
