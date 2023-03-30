import sys
sys.stdin = open('4366_input.txt')

T = int(input())

for tc in range(1, T+1):
    two = list(input())
    three = list(input())

    # print(two)
    # print(three)

    two_lst = []
    for i in range(1,len(two)):
        two = list(two)
        if two[i] == '1':
            two[i] = '0'
            two_lst.append(''.join(two))
            two[i] = '1'
        elif two[i] == '0':
            two[i] = '1'
            two_lst.append(''.join(two))
            two[i] = '0'
    # print(two_lst)

    three_lst = []

    if three[0] == '1':
        three[0] = '2'
        three_lst.append(''.join(three))
        three[0] = '1'
    else:
        three[0] = '1'
        three_lst.append(''.join(three))
        three[0] = '2'

    for i in range(1, len(three)):
        if three[i] == '1':
            three[i] = '0'
            three_lst.append(''.join(three))
            three[i] = '2'
            three_lst.append(''.join(three))
            three[i] = '1'
        elif three[i] == '2':
            three[i] = '1'
            three_lst.append(''.join(three))
            three[i] = '0'
            three_lst.append(''.join(three))
            three[i] = '2'
        elif three[i] == '0':
            three[i] = '1'
            three_lst.append(''.join(three))
            three[i] = '2'
            three_lst.append(''.join(three))
            three[i] = '0'

    # print(two_lst)
    # print(three_lst)

    result = []
    for i in two_lst:
        for j in three_lst:
            if int(i,2) == int(j,3):
                result.append(int(i,2))
    print(f'#{tc} {result[0]}')
