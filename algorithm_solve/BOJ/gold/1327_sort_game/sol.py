import sys
sys.stdin = open('1327_input.txt')

input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())
lst = list(input().split())

vis = set("".join(lst))
q = deque([(lst, 0)])
target = sorted(lst)

ans = -1

while q:
    num, cnt = q.popleft()
    if num == target:
        ans = cnt
        break
    for i in range(N - K + 1):
        tem = num[:i] + num[i:i+K][::-1] + num[i+K:]
        tem_str = "".join(tem)
        if tem_str not in vis:
            q.append((tem,cnt+1))
            vis.add(tem_str)
print(ans)




