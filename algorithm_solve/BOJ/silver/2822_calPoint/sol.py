import sys
sys.stdin = open('2822_input.txt')

input = sys.stdin.readline

lst = list(int(input()) for _ in range(8))

tem = []
ans = 0
for i in range(5):
    ans += max(lst)
    tem.append(lst.index(max(lst))+1)
    lst[lst.index(max(lst))] = -1
tem.sort()
print(ans)
print(*tem)