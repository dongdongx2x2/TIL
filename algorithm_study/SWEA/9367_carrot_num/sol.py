import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    max = count = 1

    for i in range(N-1): #[12345] i =1 2 3 4
        if arr[i] > arr[i+1]:
            count = 1
        else:
            count += 1
            if count > max:
                max = count


    print(f'#{tc}', max)