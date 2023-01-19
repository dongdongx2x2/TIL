# # 간단한 N의 약수 

# N = int(input()) # 정수 N 받기

# num_list = list(range(1,N + 1)) # 리스트 범위 설정

# for i in num_list: # 반복하면서
#     if N % i == 0: # 나누어 떨어지는 것이 약수
#         print(i)


# # List의 합 구하기

# def list_sum(N):
#     result = 0
#     for num in N: # 반복문을 통해 하나씩 더하기
#         result += num
#     return result

# print(list_sum([1, 2, 3, 4, 5]))


# # Dictionary로 이루어진 List의 합 구하기

# def dict_list_sum (dic_list):
#     result = 0
#     for i in range(len(dic_list)):       
#         result += dic_list[i]['age'] # sum() 함수 사용하지 않고 더하기

#     return result # 값 반환

# print(dict_list_sum([{'name': 'kim', 'age': 12},{'name':'lee', 'age': 4}]))

# # 2차원 List의 전체 합 구하기

# def all_list_sum (list):
#     list_sum = list[0]+ list[1] +list[2]+list[3]
#     result = 0
#     for i in list_sum:
#         result += i
#     return result
# print(all_list_sum([[1],[2, 3],[4, 5, 6],[7, 8, 9, 10]]))

# # 아스키 문자 숫자로 단어구하기

# def get_secret_word(num_list):
#     result = ''
#     for i in num_list:
#         result += chr(i)
#     return result
        
# print(get_secret_word([83, 115, 65, 102, 89]))

# # 내 이름은 몇일까??

# def get_secret_number(str_happy):
#     result = 0
#     for i in str_happy:
#         result += ord(i)
#     return result
# print(get_secret_number('happy'))


# 강한 이름

def get_secret_number(str_list1, str_list2):
    result1 = 0
    result2 = 0
    for i in str_list1:
        result1 += ord(i)
    for j in str_list2:
        result2 += ord(j)
    if result1 > result2:
        return str_list1
    elif result1 < result2:
        return str_list2
    else:
        return str_list1, str_list2

print(get_secret_number('a','a'))

