import sys
sys.stdin = open('1740_input.txt')

input = sys.stdin.readline

k = int(input())

k = bin(k)[2:]

ans = 0

for i in range(len(k)):
    if int(k[i]) == 1:
        ans += 3 ** (len(k)-i-1)
print(ans)