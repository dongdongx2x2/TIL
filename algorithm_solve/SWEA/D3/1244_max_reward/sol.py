import sys
sys.stdin = open('1244_input.txt')


def check(n):

    num = ''.join(numbers)

    if num not in ans[n]:
        ans[n].append(num)
    else:
        return

    if n == N:
        # print(numbers)
        # ans.append(''.join(numbers))
        return

    for j in range(len(numbers)):
        for i in range(j+1, len(numbers)):
            numbers[j], numbers[i] = numbers[i], numbers[j]
            # print(numbers)
            check(n+1)
            numbers[j], numbers[i] = numbers[i], numbers[j]

T = int(input())

for tc in range(1, T+1):

    numbers, N = input().split()
    numbers = list(numbers)
    max_numbers = sorted(numbers)
    N = int(N)
    # print(numbers[1])
    ans = [[] for _ in range(N+1)]
    check(0)
    print(f'#{tc} {max(ans[N])}')
    # print(max(ans))