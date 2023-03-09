import sys
sys.stdin = open('1697_input.txt')

input = sys.stdin.readline


def bfs(N):

    v[N] = 1
    q = []
    q.append(N)

    while q:

        cN = q.pop(0)
        if cN == K:
            return v[cN]
        for nN in (cN-1, cN+1, cN*2):
            if  0 <= nN < 100001 and v[nN] == 0:
                v[nN] = v[cN] + 1
                q.append(nN)



N, K = map(int, input().split())


v = [0]*100001

print(bfs(N)-1)

