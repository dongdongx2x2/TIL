import sys
sys.stdin = open('2407_input.txt')

input = sys.stdin.readline

from math import comb

n,m = map(int, input().split())
print(comb(n,m))