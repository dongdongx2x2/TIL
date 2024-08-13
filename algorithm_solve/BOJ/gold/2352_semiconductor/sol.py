import sys
sys.stdin = open('2352_input.txt')

input = sys.stdin.readline

from bisect import bisect_left

n = int(input())
ports = list(map(int, input().split()))

LIS = []

for port in ports:
    pos = bisect_left(LIS, port)

    if pos < len(LIS):
        LIS[pos] = port
    else:
        LIS.append(port)
print(len(LIS))