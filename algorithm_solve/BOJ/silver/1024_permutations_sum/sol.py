import sys
sys.stdin = open('1024_input.txt')

input = sys.stdin.readline

N, L = map(int, input().split())

for i in range(L, 101):
    tem = N - (i * (i + 1) / 2)

    if tem % i == 0:
        tem = int(tem // i)

        if tem >= -1:
            for j in range(1, i + 1):
                print(tem + j, end=' ')
            break
else:
    print(-1)


