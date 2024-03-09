import sys
sys.stdin = open('7568_input.txt')

input = sys.stdin.readline

n = int(input())
lst = []

for _ in range(n):
    w, h = map(int, input().split())
    lst.append((w, h))

for i in lst:
    tem = 1
    for j in lst:
        if i[0] < j[0] and i[1] < j[1]:
            tem += 1
    print(tem, end=' ')