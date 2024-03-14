# https://school.programmers.co.kr/learn/courses/30/lessons/17677

def check(word):
    eng = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in word:
        if i not in eng:
            return False
    return True

def solution(str1, str2):
    
    len_1 = len(str1)
    len_2 = len(str2)
    
    lst_1 = []
    for i in range(len_1 - 1):
        if check(str1[i:i+2]):
            lst_1.append(str1[i:i+2].upper())
    
    lst_2 = []
    for i in range(len_2 - 1):
        if check(str2[i:i+2]):
            lst_2.append(str2[i:i+2].upper())
    
    if not lst_1 and not lst_2:
        return 1 * 65536
    
    plus = len(lst_1 + lst_2)
         
    print(lst_1)
    print(lst_2)
    tem = []
    for i in lst_1:
        if i in lst_2:
            idx = lst_2.index(i)
            tem.append(lst_2.pop(idx))
    
    bet = len(tem)
    plus -= bet
    print(tem)
    print(bet)
    print(plus)
    answer = int(bet / plus * 65536)

    return answer