import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input()))

    ans = count = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            count = 0
        else:
            count += 1
            if ans < count:
                ans = count
    print(f'#{tc}', ans)


