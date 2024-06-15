import sys
sys.stdin = open('4134_input.txt')

input = sys.stdin.readline

import math
def prime(num):
    if num == 0 or num == 1:
        return False

    else:
        for i in range(2, int(math.sqrt(num)) + 1):
            if num% i == 0:
                return False
        return True

n = int(input())

for _ in range(n):
    num = int(input())
    while True:
        if prime(num):
            print(num)
            break
        else:
            num += 1