import sys
sys.stdin = open('16432_input.txt')

input = sys.stdin.readline
sys.setrecursionlimit(10**6)
def dfs(day, prev):
    if day == n:
        return True

    if v[day][prev]:
        return False

    v[day][prev] = True

    for rice_cake in rice_cakes[day]:
        if rice_cake != prev:
            result[day] = rice_cake
            if dfs(day+1,rice_cake):
                return True

    return False

n = int(input())

rice_cakes = []

for _ in range(n):
    lst = list(map(int, input().split()))
    rice_cakes.append(lst[1:])

result = [0] * n
v = [[False] * 10 for _ in range(n+1)]

if dfs(0, 0):
    for rice_cake in result:
        print(rice_cake)
else:
    print(-1)