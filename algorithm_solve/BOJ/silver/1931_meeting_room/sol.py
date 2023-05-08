import sys
sys.stdin = open('1931_input.txt')
input = sys.stdin.readline

N = int(input())

lst = []
for _ in range(N):
    a, b = map(int,input().split())
    lst.append((a,b))

lst.sort(key=lambda x:x[0])
lst.sort(key=lambda x:x[1])
# print(lst)
# #
tem = 0
cnt = 0
for i in lst:
    if i[0] >= tem:
        tem = i[1]
        cnt += 1
print(cnt)