import sys
sys.stdin = open('1141_input.txt')

input = sys.stdin.readline

N = int(input())

lst = list(input().rstrip() for _ in range(N))
lst.sort(key=len)

ans = 0

for i in range(N):
    flag = False

    for j in range(i+1, N):
        if lst[i]  == lst[j][:len(lst[i])]:
            flag = True
            break
    if not flag:
        ans += 1
print(ans)
