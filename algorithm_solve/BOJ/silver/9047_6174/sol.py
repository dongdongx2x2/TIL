import sys
sys.stdin = open('9047_input.txt')

input = sys.stdin.readline

def kaprekar(n):
    if n == 6174:
        return 0

    count = 0
    while n != 6174:
        count += 1
        digits = sorted(str(n).zfill(4))
        min_num = int(''.join(digits))
        max_num = int(''.join(digits[::-1]))
        n = max_num - min_num

    return count

T = int(input())
for _ in range(T):
    n = int(input())
    print(kaprekar(n))