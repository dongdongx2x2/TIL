import sys
sys.stdin = open("2108_input.txt")

input = sys.stdin.readline

n = int(input())

lst = []
for i in range(n):
    lst.append(int(input()))

lst.sort()

print(round(sum(lst)/len(lst)))
print(lst[len(lst)//2])

dic = {}

for i in lst:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

mxmx = max(dic.values())
mx_dic = []

for i in dic:
    if mxmx == dic[i]:
        mx_dic.append(i)

if len(mx_dic) > 1:
    print(mx_dic[1])
else:
    print(mx_dic[0])

print(max(lst) - min(lst))
