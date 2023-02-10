import sys
sys.stdin = open('input.txt')

T = int(input())

for _ in range(T):

    # 문자 사이사이에 .#. 이 들어 있음
    # print(' #.  A.#.P   .# '
    # 짝수일떄 홀수일때 구분

    word = input()

    print('.#.'.join('.' * (len(word) + 1)))
    print('.'+'.'.join('#'*(len(word)*2))+'.')
    print('#.' + '.#.'.join(word)+'.#')
    print('.'+'.'.join('#'*(len(word)*2))+'.')
    print('.#.'.join('.' * (len(word) + 1)))



