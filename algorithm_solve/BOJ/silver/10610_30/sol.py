import sys
sys.stdin = open('10610_input.txt')

input = sys.stdin.readline

N = sorted(input().rstrip(), reverse=True)

sm = 0
if N[-1] != '0':
    print(-1)
else:
    for i in N:
        sm += int(i)
    if sm % 3 == 0:
        print(''.join(N))
    else:
        print(-1)
