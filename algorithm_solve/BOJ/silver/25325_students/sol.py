import sys
sys.stdin = open("25325_input.txt")

input = sys.stdin.readline

n = int(input())
dic = dict()
for i in input().split():
    dic[i] = 0

for _ in range(n):
    for i in input().split():
        dic[i] += 1

for i in sorted(dic.items(), key=lambda x: (-x[1], x[0])):
    print(*i)
