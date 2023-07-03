import sys
sys.stdin = open('16198_input.txt')

input = sys.stdin.readline

def dfs(n):
    global mxmx

    if len(lst) <= 2:
        mxmx = max(mxmx, n)
        return

    for j in range(1, len(lst) - 1):
        tem = lst[j-1] * lst[j+1]

        pop_ = lst.pop(j)
        dfs(n + tem)
        lst.insert(j,pop_)

N = int(input())
lst = list(map(int,input().split()))

mxmx = 0
dfs(0)
print(mxmx)


