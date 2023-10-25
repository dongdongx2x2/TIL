import sys

sys.stdin = open("1484_input.txt")

input = sys.stdin.readline

G = int(input())

# G 킬로그램은 원래 무게 W ** 2 - w ** 2
# 16 - 1
# 64 - 49

# (8-7)*(8+7)
# (4-1)*(4+1)

s, e = 1, 1
flag = True

while s + e <= G:
    if s ** 2 - e ** 2 == G:
        print(s)
        s += 1
        flag = False

    elif s ** 2 - e ** 2 > G:
        e += 1

    else:
        s += 1
if flag:
    print(-1)
