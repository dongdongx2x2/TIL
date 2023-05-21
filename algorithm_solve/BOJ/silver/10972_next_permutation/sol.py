import sys
sys.stdin = open('10972_input.txt')

input = sys.stdin.readline


def solve(lst):
    for i in range(N - 1, 0, -1):
        if lst[i - 1] < lst[i]:
            for j in range(N - 1, 0, -1):
                if lst[i - 1] < lst[j]:
                    lst[i - 1], lst[j] = lst[j], lst[i - 1]
                    lst = lst[:i] + sorted(lst[i:])
                    print(*lst)
                    return
    print(-1)
    return

N = int(input())
lst = list(map(int,input().split()))

solve(lst)