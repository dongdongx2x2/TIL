import sys
sys.stdin = open('1107_input.txt')

input = sys.stdin.readline

n = int(input())
m = int(input())
lst = list(input().rstrip())

ans = abs(100 - n)
for num in range(1000001):
    for N in str(num):
        if N in lst:
            break
    else:
        ans = min(ans, len(str(num)) + abs(num - n))
print(ans)
