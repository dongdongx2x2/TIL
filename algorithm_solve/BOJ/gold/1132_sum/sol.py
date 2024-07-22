import sys
sys.stdin = open('1132_input.txt')

input = sys.stdin.readline

n = int(input())
alpha = [[0, False] for _ in range(10)]  # A B C ..
ans = 0
for _ in range(n):
    s = input().rstrip()
    m = 1
    alpha[ord(s[0])-ord('A')][1] = True
    for c in range(len(s)-1, -1, -1):
        alpha[ord(s[c])-ord('A')][0] += m
        m *= 10

alpha.sort()

if alpha[0][1]:
    for i in range(1, 10):
        if not alpha[i][1]:
            del alpha[i]
            break
for i in range(1, 10):
    ans += alpha[-i][0] * (10-i)
print(ans)
