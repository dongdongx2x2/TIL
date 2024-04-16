import math
import sys
sys.stdin = open('3896_input.txt')

input = sys.stdin.readline

def eratosthenes(max_num):
    arr = [True for _ in range(max_num+1)]

    for i in range(2, int(math.sqrt(max_num)) + 1):
        if arr[i] == True:
            j = 2
            while i * j <= max_num:
                arr[i*j] = False
                j += 1
    return arr

max_num = 1299709
prime_list = eratosthenes(max_num)

t = int(input())

for _ in range(t):
    k = int(input())

    if prime_list[k]:
        print(0)

    else:
        # k보다 작은 가장 큰 소수 찾기
        for before in range(k - 1, 1, -1):
            if prime_list[before]:
                break
        # k보다 큰 가장 작은 소수 찾기
        for after in range(k + 1, max_num + 1):
            if prime_list[after]:
                break
        # 길이 출력
        print(after - before)
