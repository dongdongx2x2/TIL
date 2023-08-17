import sys
sys.stdin = open('20291_input.txt')

input = sys.stdin.readline

n = int(input())

dic = {}

for _ in range(n):
    a = input().split(".")
    a = a[1]
    if not a in dic:
        dic[a] = 1
    else:
        dic[a] += 1

tem = sorted(dic.items())

for k, v in tem:
    print(k.rstrip(), v)