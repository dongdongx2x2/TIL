import sys
sys.stdin = open('11256_input.txt')

input = sys.stdin.readline

for _ in range(int(input())):
    J, N = map(int, input().split())
    lst = []
    for i in range(N):
        R, C = map(int, input().split())
        lst.append(R*C)
    lst.sort(reverse=True)
    cnt = 0
    for i in lst:
        J -= i
        cnt += 1
        if J <= 0:
            print(cnt)
            break