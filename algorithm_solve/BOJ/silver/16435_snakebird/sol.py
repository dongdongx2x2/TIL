import sys
sys.stdin = open('16435_input.txt')

input = sys.stdin.readline

N, L = map(int, input().split())

height = list(map(int, input().split()))

height.sort()

for i in height:
    if i > L:
        break
    elif i <= L:
        L += 1

print(L)