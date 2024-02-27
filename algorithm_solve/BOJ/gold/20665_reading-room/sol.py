import sys
sys.stdin = open('20655_input.txt')

input = sys.stdin.readline

n, t, p = map(int, input().split())


time = [[0] * n for _ in range(720)]

data = []

for _ in range(t):
    s, e = map(int, input().split())
    s = (s//100 - 9) * 60 + s % 100
    e = (e//100 - 9) * 60 + e % 100
    if s == e:
        continue
    data.append((s,e))

data.sort(key=lambda x: (x[0], x[1]))

for start, end in data:
    mx_dis = 0
    seat = 0

    used = []

    # 이미 차있는 좌석 찾기
    for i in range(n):
        if time[start][i]:
            used.append(i)

    # 빈 좌석 돌리기
    for i in range(n):
        if time[start][i]:
            continue

        # 빈 좌석중 차있는 좌석과의 거리
        dis = 1000
        for u in used:
            gap = abs(u-i)
            dis = min(dis, gap)

        if mx_dis < dis:
            mx_dis = dis
            seat = i

    for t in range(start, end):
        time[t][seat] = 1

ans = 0
for i in range(720):
    if not time[i][p-1]:
        ans += 1
print(ans)