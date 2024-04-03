import sys
sys.stdin = open('1039_input.txt')

input = sys.stdin.readline

from collections import deque

def bfs(n, k):
    q = deque()
    q.append((str(n), 0))
    v = set()
    v.add((str(n),0))

    mxmx = -1

    while q:
        cur, cnt = q.popleft()

        if cnt == k:
            mxmx = max(mxmx, int(cur))

        elif cnt < k:
            for i in range(len(cur)):
                for j in range(i+1, len(cur)):
                    if i == 0 and cur[j] == '0':
                        continue

                    new_num = list(cur)
                    new_num[i], new_num[j] = new_num[j], new_num[i]
                    new_str = ''.join(new_num)
                    if (new_str, cnt + 1) not in v:
                        v.add((new_str, cnt + 1))
                        q.append((new_str, cnt + 1))
    return mxmx

n, k = map(int, input().split())

ans = bfs(n,k)
print(ans)