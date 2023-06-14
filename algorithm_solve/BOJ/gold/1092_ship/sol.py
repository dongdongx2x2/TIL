import sys
sys.stdin = open('1092_input.txt')

input = sys.stdin.readline

def solve(N, M, lst, lst2):
    if lst[0] < lst2[0]:
        return -1

    cnt = 0

    while lst2:
        for i in lst:
            if lst2 and i < lst2[-1]:
                continue
            for j in lst2:
                if i >= j:
                    lst2.remove(j)
                    break
        cnt += 1
    return cnt



N = int(input())
lst = list(map(int,input().split()))
M = int(input())
lst2 = list(map(int,input().split()))

lst.sort(reverse=True)
lst2.sort(reverse=True)

# print(lst)
# print(lst2)
print(solve(N,M,lst,lst2))