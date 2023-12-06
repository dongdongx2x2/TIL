import sys
sys.stdin = open('11501_input.txt')

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    lst = list(map(int, input().split()))

    lst = lst[::-1]

    sm = 0 # 총이익
    mx = 0 # 최댓값

    for i in range(N):
        if lst[i] > mx:
            mx = lst[i]
        else:
            sm += mx - lst[i]
    print(sm)
