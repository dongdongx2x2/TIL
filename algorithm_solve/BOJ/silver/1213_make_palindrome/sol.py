import sys
sys.stdin = open('1213_input.txt')

input = sys.stdin.readline

from collections import Counter

lst = list(input().rstrip())

lst.sort()
check = Counter(lst)

cnt = 0
center = ""

for i in check:
    if check[i] % 2 != 0:
        cnt += 1
        center += i
        lst.remove(i)

    if cnt > 1:
        break
if cnt > 1:
    print("I'm Sorry Hansoo")
else:
    res = ""
    for i in range(0, len(lst), 2):
        res += lst[i]
    print(res + center + res[::-1])