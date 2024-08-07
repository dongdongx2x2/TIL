import sys

sys.stdin = open('1283_input.txt')

input = sys.stdin.readline

def solve():
    flag = False
  
    for i in range(len(lst)):
        if lst[i][0].upper() not in v:
            v.add(lst[i][0].upper())
            flag = True 
            lst[i] = '[' + lst[i][0] + ']' + lst[i][1:]
            print(' '.join(lst)) 
            return

    if not flag:
        for i in range(len(lst)):
            for j in range(len(lst[i])):
                if lst[i][j].upper() not in v:
                    v.add(lst[i][j].upper())
                    lst[i] = lst[i][:j] + '[' + lst[i][j] + ']' + lst[i][j+1:]
                    print(' '.join(lst))
                    return
    if not flag:
        print(' '.join(lst))
        return

n = int(input())
v = set()
for _ in range(n):
    lst = input().split()

    solve()
          
        