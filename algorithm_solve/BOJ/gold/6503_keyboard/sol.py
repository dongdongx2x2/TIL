import sys
sys.stdin = open('6503_input.txt')

input = sys.stdin.readline
from collections import defaultdict

def max_str_length(m, s):
    n = len(s)

    if n == 0:
        return 0

    left = 0
    right = 0
    char_count = defaultdict(int)
    max_length = 0
    distinct_count = 0

    while right < n:
        if char_count[s[right]] == 0:
            distinct_count += 1
        char_count[s[right]] += 1
        right += 1

        while distinct_count > m:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                distinct_count -= 1
            left += 1

        max_length = max(max_length, right - left)

    return max_length

while True:
    m = int(input())
    if m == 0:
        break

    s = input().rstrip()
    result = max_str_length(m, s)
    print(result)
