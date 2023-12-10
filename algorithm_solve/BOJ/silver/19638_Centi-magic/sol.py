import sys
sys.stdin = open('19638_input.txt')

input = sys.stdin.readline

import heapq

N, H, T = map(int, input().split())


lst = []

for _ in range(N):
    heapq.heappush(lst, -int(input()))

cnt = 0
for i in range(T):
    tem = heapq.heappop(lst)

    if -tem < H:
        heapq.heappush(lst, tem)
        break
    elif -tem == 1:
        heapq.heappush(lst, tem)

    else:
        tem = -(abs(tem) // 2)
        # print(tem)
        heapq.heappush(lst, tem)
        cnt += 1

if -min(lst) < H:
    print('YES')
    print(cnt)
else:
    print("NO")
    print(-heapq.heappop(lst))