import sys
sys.stdin = open('7490_input.txt')

input = sys.stdin.readline

def dfs(n, idx, rst):
    if idx == n:
        ans = eval(rst.replace(" ", ""))
        if ans == 0:
            result.append(rst)
        return

    dfs(n, idx+1, rst + " " + str(idx+1))
    dfs(n, idx+1, rst + "+" + str(idx+1))
    dfs(n, idx+1, rst + "-" + str(idx+1))

t = int(input())

for _ in range(t):
    n = int(input())
    result = []
    dfs(n, 1, "1")
    for r in result:
        print(r)
    print()