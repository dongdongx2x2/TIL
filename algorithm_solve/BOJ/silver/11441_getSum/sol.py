import sys
sys.stdin = open('11441_input.txt')

input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

m = int(input())

sm_lst = [lst[0]]

for i in range(1, n):
    sm_lst.append(sm_lst[-1] + lst[i])

for _ in range(m):
    i, j = map(int, input().split())
    if i == 1:
        print(sm_lst[j-1])

    else:
        print(sm_lst[j-1] - sm_lst[i-2])