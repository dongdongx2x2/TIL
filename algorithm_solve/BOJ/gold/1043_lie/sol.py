import sys
sys.stdin = open('1043_input.txt')

input = sys.stdin.readline

N, M = map(int,input().split())

klst = list(map(int,input().split()))

k = klst[0]
true_lst = set(klst[1:])

party = []
for _ in range(M):
    rlst = list(map(int,input().split()))
    r = rlst[0]
    rlst = set(rlst[1:])
    party.append(rlst)
# print(party)


cnt = [1] * M

for _ in range(M):
    for idx, sset in enumerate(party):
        if true_lst & sset:
            cnt[idx] = 0
            true_lst = true_lst | sset
print(sum(cnt))

