import sys
sys.stdin = open('11509_input.txt')

input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

h = [0] * 10000001

for i in lst:
    if h[i] == 0:
        h[i-1] += 1
    else:
        h[i] -= 1
        h[i-1] += 1
print(sum(h))




