import sys
sys.stdin = open("1337_input.txt")

input = sys.stdin.readline

N = int(input())

lst = [int(input()) for _ in range(N)]
lst.sort()

tem = []

for i in range(N):
    cnt = 0
    for j in range(lst[i], lst[i] +5):
        if j not in lst:
            cnt += 1
    tem.append(cnt)
print(min(tem))