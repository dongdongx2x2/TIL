import sys
sys.stdin = open('1966_input.txt')

input = sys.stdin.readline

from collections import deque

T = int(input())

for _ in range(T):
    N, M = map(int,input().split())
    lst = deque(list(map(int,input().split())))

    cnt = 0
    while lst:
        mx = max(lst)
        tem = lst.popleft()
        M -= 1

        if tem == mx:
            cnt += 1
            if M == -1:
                print(cnt)
                break
        else:
            lst.append(tem)
            if M == -1:
                M = len(lst) -1



