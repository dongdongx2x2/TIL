import sys
sys.stdin = open('12919_input.txt')

input = sys.stdin.readline

def dfs(string):
    global ans

    if string == s:
        ans = 1
        return

    if len(string) < len(s):
        return

    if string[-1] == 'A':
        dfs(string[:-1])

    if string[0] == 'B':
        dfs(string[1:][::-1])

s = input().rstrip()
t = input().rstrip()

ans = 0
dfs(t)
print(ans)

