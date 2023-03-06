import sys
sys.stdin = open('input.txt')

def search(lst):
    while True:
        for i in range(1, 6):
            a = lst.pop(0) - i
            if a > 0:
                lst.append(a)
            else:
                lst.append(0)
                return lst

for _ in range(10):
    tc = int(input())

    lst = list(map(int, input().split()))

    print(f'#{tc}', *search(lst))
