import sys
sys.stdin = open("1747_input.txt")

input = sys.stdin.readline

def prime(x):
    if x == 1:
        return False

    for i in range(2, int(x**0.5) + 1):
        if not x % i:
            return False

    return True

N = int(input())

while True:
    if str(N) == str(N)[::-1] and prime(N):
        print(N)
        break
    N += 1

