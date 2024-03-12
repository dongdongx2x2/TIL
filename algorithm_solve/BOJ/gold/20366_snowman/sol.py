import sys
sys.stdin = open('20366_input.txt')

input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
lst.sort()

ans = 1e9

for i in range(n):
    for j in range(i + 3, n):
        left, right = i+1, j-1

        while left < right:
            tem = (lst[i] + lst[j]) - (lst[left] + lst[right])

            if abs(ans) > abs(tem):
                ans = abs(tem)

            if tem < 0:
                right -= 1

            elif tem > 0:
                left += 1
            else:
                print(0)
                exit()
print(ans)



