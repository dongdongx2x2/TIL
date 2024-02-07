import sys
sys.stdin = open('2448_input.txt')

input = sys.stdin.readline

def solve(i, j, cnt):
    if cnt == 3:
        stars[i][j] = "*"
        stars[i+1][j-1] = stars[i+1][j+1] = "*"

        for k in range(-2, 3):
            stars[i+2][j-k] = "*"
        return

    next_cnt = cnt // 2
    solve(i, j, next_cnt)
    solve(i + next_cnt, j - next_cnt, next_cnt)
    solve(i+ next_cnt, j + next_cnt, next_cnt)

n = int(input())

stars = [[' ']*(2*n-1) for _ in range(n)]

solve(0, (2*n-1)//2, n)
for star in stars:
    print("".join(star))