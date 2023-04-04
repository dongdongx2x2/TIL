import sys
sys.stdin = open('14675_input.txt')

input = sys.stdin.readline

N = int(input())

arr = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

Q = int(input())
for _ in range(Q):
    a, b = map(int, input().split())

    if a == 2:
        print('yes')

    elif a == 1:
        if len(arr[b]) == 1:
            print('no')
        else:
            print('yes')

