import sys
sys.stdin = open('2661_input.txt')

input = sys.stdin.readline

def is_good(num):
    length = len(num)
    for i in range(1, length//2 + 1):
        if num[-i:] == num[-2*i:-i]:
            return False
    return True

def backtracking(num):
    if len(num) == n:
        print(num)
        return True

    for i in "123":
        if is_good(num + i):
            if backtracking(num + i):
                return True

    return False
n = int(input())
backtracking("")