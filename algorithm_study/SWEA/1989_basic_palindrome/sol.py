import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):

    n = input()

    result = 0
    if n == n[::-1]:
        result += 1

    print(f'#{tc} {result}')
