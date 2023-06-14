import sys
sys.stdin = open('5430_input.txt')

input = sys.stdin.readline

from collections import deque


def solve(p,q):


    flag = 0

    for i in p:
        if i == 'R':
            flag += 1
        elif i == 'D':
            if q:
                if flag % 2:
                    q.pop()
                else:
                    q.popleft()
            else:
                return 'error'

    if flag % 2:
        q.reverse()

    return '['+ ','.join(q) + ']'

T = int(input())

for _ in range(T):
    p = input().rstrip()
    n = int(input())
    lst = input().rstrip()
    lst = lst[1:-1].split(',')
    # lst = lst.split(',')
    q = deque(lst)
    if n == 0:
        q = deque()
    print(solve(p,q))


