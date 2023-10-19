import sys
sys.stdin = open('1253_input.txt')

input = sys.stdin.readline

N = int(input())

lst = list(map(int, input().split()))
lst.sort()

ans = 0
for i in range(N):

    tem = lst[:i] + lst[i+1:]
    s, e = 0, len(tem) - 1

    while s < e:
        if lst[i] == tem[s] + tem[e]:
            ans += 1
            break
        elif lst[i] > tem[s] + tem[e]:
            s += 1
        else:
            e -= 1
print(ans)