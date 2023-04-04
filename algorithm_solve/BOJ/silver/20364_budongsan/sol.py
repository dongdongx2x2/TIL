import sys
sys.stdin = open('20364_input.txt')

input = sys.stdin.readline

N, Q = map(int, input().split())

# v = []
# duck = []
# for _ in range(Q):
#     duck.append(int(input()))
#
# for num in duck:
#     ans = 0
#     tem = num
#     while num > 1:
#
#         if num in v:
#             ans = num
#         num = num // 2
#     v.append(tem)
#
#     print(ans)

v = [0] * (N+1)
for _ in range(Q):
    num = int(input())

    ans = 0
    tem = num
    while num > 1:
        if v[num]:
            ans = num
        num = num // 2
    v[tem] = 1
    print(ans)