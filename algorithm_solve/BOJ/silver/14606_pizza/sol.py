import sys

sys.stdin = open("14606_input.txt")

input = sys.stdin.readline

N = int(input())
print(N * (N - 1) // 2)
