import sys
sys.stdin = open('1105_input.txt')

input = sys.stdin.readline

a, b = input().split()

ans = 0

if len(a) != len(b):
    print(0)

else:
    for i in range(len(a)):
        if a[i] == b[i]:
            if a[i] == '8':
                ans += 1
        else:
            break
    print(ans)