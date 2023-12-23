import sys
sys.stdin = open('20044_input.txt')

input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

lst.sort()

ans = []
for i in range(len(lst)):
    tem = lst[i] + lst[::-1][i]
    ans.append(tem)

print(min(ans))
