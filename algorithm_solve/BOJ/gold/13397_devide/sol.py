import sys
sys.stdin = open('13397_input.txt')

input = sys.stdin.readline

def can_divide(max_score):
    cnt = 1
    cur_max = cur_min = lst[0]

    for num in lst[1:]:
        cur_max = max(cur_max, num)
        cur_min = min(cur_min, num)

        if cur_max - cur_min > max_score:
            cnt += 1
            cur_max = cur_min = num

        if cnt > m:
            return False

    return True

n, m = map(int, input().split())
lst = list(map(int, input().split()))

left, right = 0, max(lst) - min(lst)

while left <= right:
    mid = (left + right) // 2

    if can_divide(mid):
        result = mid
        right = mid - 1

    else:
        left = mid + 1
print(result)