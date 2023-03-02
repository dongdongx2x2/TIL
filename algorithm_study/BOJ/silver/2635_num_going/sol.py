import sys
sys.stdin = open('2635_input.txt')

input = sys.stdin.readline

def cnt(n):
    lst = [N]
    lst.append(n)
    while lst[-2]-lst[-1] >= 0:
        lst.append(lst[-2]-lst[-1])
    return lst


N = int(input())

mx = 0
for i in range(1, N+1):
    if mx < len(cnt(i)):
        mx = len(cnt(i))
        lst = cnt(i)
print(mx)
print(*lst)

