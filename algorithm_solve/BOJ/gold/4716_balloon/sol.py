import sys
sys.stdin = open('4716_input.txt')

input = sys.stdin.readline

while True:
    n, a, b = map(int, input().split())
    if n == a == b == 0:
        break

    teams = []
    for _ in range(n):
        k, da, db = map(int, input().split())
        teams.append((k, da, db))

    total_dis = 0
    teams.sort(key=lambda x: abs(x[1] - x[2]), reverse=True)

    for k, da, db in teams:
        if da < db:  # A가 더 가까운 경우
            if a >= k:
                total_dis += k * da
                a -= k
            else:
                total_dis += a * da + (k - a) * db
                b -= (k - a)
                a = 0
        else:  # B가 더 가까운 경우
            if b >= k:
                total_dis += k * db
                b -= k
            else:
                total_dis += b * db + (k - b) * da
                a -= (k - b)
                b = 0

    print(total_dis)