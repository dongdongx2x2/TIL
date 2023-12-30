import sys

sys.stdin = open('15736_input.txt')

input = sys.stdin.readline

import math

n = int(input())
print(int(math.sqrt(n)))
