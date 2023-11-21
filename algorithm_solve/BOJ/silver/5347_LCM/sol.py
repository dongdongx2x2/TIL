import sys
sys.stdin = open('5347_input.txt')

input = sys.stdin.readline

from math import gcd

def lcm(x, y):
    return x * y // gcd(x, y)

n = int(input())

for _ in range(n):
    x, y = map(int, input().split())
    print(lcm(x, y))