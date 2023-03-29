import sys
sys.stdin = open('5207_input.txt')

def check(n):
    global cnt

    s = 0
    e = len(a) - 1

    flag = 0
    while s <= e:

        mid = (s + e)//2

        if a[mid] == n:
            cnt += 1
            return

        elif n < a[mid]:
            if flag == 1:
                break
            e = mid - 1
            flag = 1

        else:
            if flag == 2:
                break
            s = mid + 1
            flag = 2

T = int(input())

for tc in range(1, T+1):

    N, M = map(int, input().split())
    a = sorted(list(map(int,input().split())))
    b = list(map(int,input().split()))

    cnt = 0
    for i in b:
        check(i)
    print(f'#{tc} {cnt}')
