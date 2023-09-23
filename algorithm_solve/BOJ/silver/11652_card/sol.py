import sys
sys.stdin = open('11652_input.txt')

input = sys.stdin.readline

n = int(input())

dic = {}

for i in range(n):
    a = int(input())

    if a in dic:
        dic[a] += 1
    else:
        dic[a] = 1

ans = sorted(dic.items(),key = lambda x : (-x[1],x[0]))

print(ans[0][0])