import sys
sys.stdin = open('8394_input.txt')

input = sys.stdin.readline

n = int(input())

a, b = 1, 0

for i in range(n):
    a, b = (a + b) % 10, a % 10

print(a)
