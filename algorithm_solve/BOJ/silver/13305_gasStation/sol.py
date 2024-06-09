import sys
sys.stdin = open('13305_input.txt')

input = sys.stdin.readline

n = int(input())
load = list(map(int, input().split()))
price = list(map(int, input().split()))

minPrice = price[0]
ans = 0

for i in range(n-1):
    if minPrice > price[i]:
        minPrice = price[i]

    ans += minPrice * load[i]
print(ans)