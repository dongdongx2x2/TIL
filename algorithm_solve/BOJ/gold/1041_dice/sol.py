import sys
sys.stdin = open('1041_input.txt')

input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

# abc, abd, ade, ace, fbc, fbd, fde, fce 8가지 - 3개면
# 123,124,145,135, 623,624,625,635
#
abc = lst[0] + lst[1] + lst[2]
abd = lst[0] + lst[1] + lst[3]
ade = lst[0] + lst[3] + lst[4]
ace = lst[0] + lst[2] + lst[4]
fbc = lst[5] + lst[1] + lst[2]
fbd = lst[5] + lst[1] + lst[3]
fde = lst[5] + lst[3] + lst[4]
fce = lst[5] + lst[2] + lst[4]

three_min = min(abc, abd, ade, ace, fbc, fbd, fde, fce)

#ab,ac,ad, ae, fb,fc,fd,fe - 8가지 - 2개면

ab = lst[0] + lst[1]
ac = lst[0] + lst[2]
ad = lst[0] + lst[3]
ae = lst[0] + lst[4]
fb = lst[5] + lst[1]
fc = lst[5] + lst[2]
fd = lst[5] + lst[3]
fe = lst[5] + lst[4]
bc = lst[1] + lst[2]
bd = lst[1] + lst[3]
de = lst[3] + lst[4]
ce = lst[2] + lst[4]

two_min = min(ab,ac,ad,ae,fb,fc,fd,fe,bc,bd,de,ce)

mimi = min(lst)


a = two_min * (((n-1) * 4) + ((n-2) * 4))
b = three_min * 4
c = (mimi * ((n-2) * (n-1))) * 4 + mimi * (n-2)**2

if n == 1:
    print(sum(lst) - max(lst))
else:
    print(a + b + c)


