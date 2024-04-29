import sys
sys.stdin = open('10800_input.txt')

input = sys.stdin.readline

n = int(input())

ball = []
for i in range(n):
    c, s = map(int, input().split())
    ball.append((s, c, i))

ball.sort()

result = [0] * n

same = [0] * (n+1)
sm = 0
j = 0
print(ball)
for i in range(n):
    while ball[j][0] < ball[i][0]:
        sm += ball[j][0]
        same[ball[j][1]] += ball[j][0]
        j += 1

    result[ball[i][2]] = sm - same[ball[i][1]]

for r in result:
    print(r)

