import sys
sys.stdin = open('2457_input.txt')

input = sys.stdin.readline

N = int(input())

date = []
for _ in range(N):
    m1, d1, m2, d2 = map(int, input().split())
    date.append((m1 * 100 + d1, m2 * 100 + d2))

date.sort()

cnt = 0
e = 0

tem = 301

while date:
    if tem >= 1201 or tem < date[0][0]:
        break

    for i in range(len(date)):
        if tem >= date[0][0]:
            if e <= date[0][1]:
                e = date[0][1]
            date.remove(date[0])

        else:
            break
    tem = e
    cnt += 1

if tem < 1201:
    print(0)
else:
    print(cnt)