import sys
sys.stdin = open('1713_input.txt')

input = sys.stdin.readline

N = int(input())
T = int(input())
lst = list(map(int, input().split()))

dic = {}
tem = []

for i in lst:
    if len(tem) < N:
        if i not in tem:
            tem.append(i)
        dic[i] = dic.get(i, 0) + 1

    else:
        if i in tem:
            dic[i] = dic.get(i, 0) + 1
        else:
            for k, v in dic.items():
                if v == min(dic.values()):
                    mimi = k
                    break
            # print(mimi)
            dic.pop(mimi)
            idx = tem.index(mimi)
            tem.pop(idx)

            tem.insert(idx, i)
            dic[i] = dic.get(i,0) + 1
tem.sort()
print(*tem)
