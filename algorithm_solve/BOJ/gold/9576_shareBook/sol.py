import sys
sys.stdin = open('9576_input.txt')

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    requests = []
    for _ in range(m):
        a, b = map(int, input().split())
        requests.append((a, b))

    requests.sort(key=lambda x:(x[1], x[0]))

    cnt = 0
    give = [0] * (n + 1)

    for a, b in requests:
        for book in range(a, b + 1):
            if not give[book]:
                give[book] = 1
                cnt += 1
                break
    print(cnt)