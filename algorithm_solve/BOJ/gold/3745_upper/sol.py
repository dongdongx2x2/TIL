import sys
sys.stdin = open('3745_input.txt')

input = sys.stdin.readline

from bisect import bisect_left

while True:
    try:
        n = int(input())
        lst = list(map(int, input().split()))

        LIS = []

        for l in lst:
            pos = bisect_left(LIS, l)

            if pos < len(LIS):
                LIS[pos] = l
            else:
                LIS.append(l)

        print(len(LIS))

    except:
        break