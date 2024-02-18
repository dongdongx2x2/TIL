import sys
sys.stdin = open('4375_input.txt')

input = sys.stdin.readline

while True:
    try:
        n = int(input())
    except:
        break
    i = 1
    cnt = 1
    while True:
        if i % n != 0:
            i = i * 10 + 1
            cnt += 1
        else:
            break
    print(cnt)