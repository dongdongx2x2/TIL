import sys
sys.stdin = open('2493_input.txt')

input = sys.stdin.readline

N = int(input())
lst = list(map(int,input().split()))

tem = []
ans = [0] * N

for i in range(N):
    while tem:
        if tem[-1][1] > lst[i]:
            ans[i] = tem[-1][0] + 1
            break
        else:
            tem.pop()
    tem.append((i,lst[i]))
print(*ans)