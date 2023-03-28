import sys
sys.stdin = open('5202_input.txt')

T = int(input())

for tc in range(1, T+1):

    N = int(input())

    lst = []
    for _ in range(N):
        s, e = map(int,input().split())
        lst.append((s,e))
    lst.sort(key=lambda x:x[1])

    result = 0
    end = 0

    for s, e in lst:
        if end <= s:
            result += 1
            end = e
    print(f'#{tc} {result}')
