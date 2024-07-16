import sys
sys.stdin = open('2643_input.txt')

input = sys.stdin.readline

n = int(input())
papers = []
for _ in range(n):
    a, b = map(int, input().split())
    papers.append((min(a,b), max(a,b)))

papers.sort(key=lambda x: x[0] * x[1], reverse=True)

dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if (papers[i][0] <= papers[j][0] and papers[i][1] <= papers[j][1]) or \
            (papers[i][0] <= papers[j][1] and papers[i][1] <= papers[j][0]):
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))