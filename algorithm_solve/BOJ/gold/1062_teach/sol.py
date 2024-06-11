import sys
sys.stdin = open('1062_input.txt')

input = sys.stdin.readline

n, k = map(int, input().split())

def count_read(words, learned):
    cnt = 0

    for w in words:
        for c in w:
            if not learned[ord(c) - ord('a')]:
                break
        else:
            cnt += 1
    return cnt

def dfs(idx, cnt):
    global mxmx

    if cnt == k - 5:
        mxmx = max(mxmx, count_read(words, learned))
        return

    for i in range(idx, 26):
        if not learned[i]:
            learned[i] = 1
            dfs(i+1, cnt + 1)
            learned[i] = 0

words = [input().rstrip() for _ in range(n)]

if k < 5:
    print(0)

else:
    learned = [0] * 26

    for c in "antic":
        learned[ord(c) - ord('a')] = 1

    mxmx = 0
    dfs(0, 0)
    print(mxmx)