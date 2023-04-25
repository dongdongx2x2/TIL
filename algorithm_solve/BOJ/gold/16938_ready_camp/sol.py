import sys
sys.stdin = open('16938_input.txt')

input = sys.stdin.readline

N, L, R, X = map(int, input().split())

lst = list(map(int, input().split()))

cnt = 0
for i in range(1,1<<N):
    tem = []
    for j in range(N):
        if i & (1<<j):
            tem.append(lst[j])
    if L<=sum(tem)<=R and max(tem)-min(tem) >=X:
        cnt += 1
print(cnt)
