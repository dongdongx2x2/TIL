import sys
sys.stdin = open('13414_input.txt')

input = sys.stdin.readline

k, l = map(int, input().split())

dic = {}

for i in range(l):
    dic[input().rstrip()] = i

result = sorted(dic.items(), key = lambda x:x[1])

if (k > len(result)):
    k = len(result)

for i in range(k):
    print(result[i][0])