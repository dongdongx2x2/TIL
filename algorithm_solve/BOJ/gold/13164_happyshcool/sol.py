import sys
sys.stdin = open('13164_input.txt')

input = sys.stdin.readline

N, K = map(int,input().split())

lst = list(map(int,input().split()))

dis = []
for i in range(1, N):
    dis.append(lst[i]-lst[i-1])
dis.sort()
print(sum(dis[:N-K]))