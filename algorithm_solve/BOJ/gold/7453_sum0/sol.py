import sys
sys.stdin = open('7453_input.txt')

input = sys.stdin.readline

n = int(input())

A, B, C, D = [], [], [], []

for _ in range(n):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

ab, cd = [] , []

for i in range(n):
    for j in range(n):
        ab.append(A[i] + B[j])
        cd.append(C[i] + D[j])

ab.sort()
cd.sort()

cnt = 0

left, right = 0, len(cd) - 1

while left < len(ab) and right >= 0:
    cur_sum = ab[left] + cd[right]

    if cur_sum == 0:
        left_cnt, right_cnt = 1, 1

        while left + 1 < len(ab) and ab[left] == ab[left + 1]:
            left += 1
            left_cnt += 1

        while right - 1 >= 0 and cd[right] == cd[right - 1]:
            right -= 1
            right_cnt += 1

        cnt += left_cnt * right_cnt
        left += 1
        right -= 1

    elif cur_sum < 0:
        left += 1

    else:
        right -= 1

print(cnt)