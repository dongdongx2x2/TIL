import sys

sys.stdin = open('3036_input.txt')

input = sys.stdin.readline

from math import gcd

n = int(input())
lst = list(map(int, input().split()))

for i in range(1, n):
    t = gcd(lst[0], lst[i])
    print(f'{lst[0] // t}/{lst[i] // t}')
