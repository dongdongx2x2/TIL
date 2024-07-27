import sys
sys.stdin = open('5426_input.txt')

input = sys.stdin.readline

t = int(input())

for i in range(t):
    message = input().rstrip()

    n = int(len(message) ** (1 / 2))

    ans = ""
    for j in range(n, 0, -1):
        for k in range(j, n ** 2 + 1, n):
            ans += message[k-1]

    print(ans)
