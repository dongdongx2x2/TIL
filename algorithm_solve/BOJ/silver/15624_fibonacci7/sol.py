import sys
sys.stdin = open('15624_input.txt')

input = sys.stdin.readline

n = int(input())
a, b = 0, 1
for i in range(n):
    a, b = (a + b) % 1000000007, a % 1000000007
print(a)
