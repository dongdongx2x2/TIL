import sys
sys.stdin = open('2212_input.txt')

input = sys.stdin.readline

N = int(input())
K = int(input())

lst = list(map(int,input().split()))
lst.sort()

tem = []
for i in range(1, N):
    tem.append(lst[i]-lst[i-1])
tem.sort()

print(sum(tem[:N-K]))