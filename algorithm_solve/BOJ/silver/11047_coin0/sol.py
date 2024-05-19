import sys
sys.stdin = open('11047_input.txt')

input = sys.stdin.readline

n, k = map(int, input().split())
lst = list()
for i in range(n):
    lst.append(int(input()))

count = 0
for i in reversed(range(n)):
    count += k // lst[i]
    k %= lst[i]

print(count)
