import sys
sys.stdin = open('18870_input.txt')

input = sys.stdin.readline

N = int(input())

lst = list(map(int,input().split()))
lst2 = sorted(list(set(lst)))

dict = {}

for i in range(len(lst2)):
    dict[lst2[i]] = i

for i in lst:
    print(dict[i], end=' ')
