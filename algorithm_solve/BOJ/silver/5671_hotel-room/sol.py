import sys
sys.stdin = open('5671_input.txt')

input = sys.stdin.readline

while True:

    data = input().rstrip()

    if not data:
        break
    res = 0
    a, b = data.split()
    for i in range(int(a), int(b) + 1):
        if len(set(str(i))) == len(str(i)):
            res += 1
    print(res)