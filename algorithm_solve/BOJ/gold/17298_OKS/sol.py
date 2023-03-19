import sys
sys.stdin = open('17298_input.txt')

input = sys.stdin.readline

N = int(input())

lst = list(map(int, input().split()))

stack = []
result = [-1] * N


for i in range(N):

    while stack and lst[i] > stack[-1][1]:
        idx, n = stack.pop()
        result[idx] = lst[i]
    stack.append((i,lst[i]))

print(*result)
