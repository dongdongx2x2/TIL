import sys
sys.stdin = open('1946_input.txt')

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())

    # cnt = N
    lst = []
    for _ in range(N):
        a, b = map(int, input().split())
        lst.append((a,b))
    lst.sort()

    cnt = 0

    good = lst[0][1]
    for j in range(1, N):
        if good > lst[j][1]:
            cnt += 1
            good = lst[j][1]

    print(cnt+1)