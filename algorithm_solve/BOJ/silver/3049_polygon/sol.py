import sys

sys.stdin = open('3049_input.txt')

input = sys.stdin.readline

n = int(input())
print(int(n*(n-1)*(n-2)*(n-3)/24))