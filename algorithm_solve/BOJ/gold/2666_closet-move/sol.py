import sys
sys.stdin = open('2666_input.txt')

input = sys.stdin.readline

def dfs(open1, open2, depth, cnt):
    global mimi

    if depth == m:
        mimi = min(mimi, cnt)
        return

    if cnt >= mimi:
        return

    dfs(lst[depth], open2, depth+1, cnt+abs(open1-lst[depth]))
    dfs(open1, lst[depth], depth+1, cnt+abs(open2-lst[depth]))

n = int(input())
s1, s2 = map(int, input().split())
m = int(input())
lst = [int(input()) for _ in range(m)]

mimi = 1e9

dfs(s1, s2, 0, 0)
print(mimi)


