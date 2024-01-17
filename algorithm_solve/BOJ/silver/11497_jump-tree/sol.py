import sys
sys.stdin = open('11497_input.txt')

input = sys.stdin.readline

t = int(input())

for i in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    lst.sort()
    ans = 0

    for j in range(2, n):
        ans = max(ans, abs(lst[j]-lst[j-2]))
    print(ans)
