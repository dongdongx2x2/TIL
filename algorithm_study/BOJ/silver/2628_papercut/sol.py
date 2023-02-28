import sys
# sys.stdin = open('2628_input.txt')
input = sys.stdin.readline

G, S = map(int, input().split())

N = int(input())

Glst = []
Slst = []
for _ in range(N):
    i, n = map(int,input().split())
    if i == 1:
        Slst.append(n)
    else:
        Glst.append(n)
Glst.append(0)
Glst.append(S)
Slst.append(0)
Slst.append(G)
Glst.sort()
Slst.sort()
# 줄이 3개면 6 개가 나옴
a = []
b = []
for i in range(len(Glst)-1):
    a.append(Glst[i+1]-Glst[i])
for i in range(len(Slst)-1):
    b.append(Slst[i+1]-Slst[i])

print(max(a)*max(b))
# result = []
# for i in a:
#     for j in b:
#         result.append(i*j)
# print(max(result))




