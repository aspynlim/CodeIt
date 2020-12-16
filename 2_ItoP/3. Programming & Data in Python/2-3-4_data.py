########## 01. Aliasing ##########
x = [1, 2, 3, 4, 5]
y = x
y[2] = -100
print(x)  # [1, 2, -100, 4, 5]
print(y)  # [1, 2, -100, 4, 5]

print('----------------')

x = [-10, -20, -30, -40, -50]
y = list(x)
z = x

x[0] = 'x'
y[1] = 'y'
z[2] = 'z'

print(x)  # ['x', -20, 'z', -40, -50]
print(y)  # [-10, 'y', 700, -40, -50]
print(z)  # ['x', -20, 'z', -40, -50]


########## 02. List & String ##########
# 인덱싱 (Indexing)
alphabet_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
print(alphabet_list[0])   # A
print(alphabet_list[-1])  # J
print(alphabet_list[:5])  # ['A', 'B', 'C', 'D', 'E']


# 슬라이싱 (Slicing)
alphabet_string = 'ABCDEFGHIJ'
print(alphabet_string[0])  # A
print(alphabet_string[-1]) # J
print(alphabet_string[:5]) # ABCDE


# for 반복문
for alphabet in alphabet_list:
    print(alphabet)


# 덧셈 연산 + len 함수 + Mutable (수정 가능) vs. Immutable (수정 불가능)
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
list_3 = list_1 + list_2
list_3[0] = -100
print(list_3)  # [-100, 2, 3, 4, 5, 6]
print(len(list_3))  # 6

str_1 = 'Hello'
str_2 = 'World'
str_3 = str_1 + str_2
# str_3[0] = 'x'
# TypeError: 'str' object does not support item assignment (문자열 자체를 수정할 수는 없음)
print(str_3)  # 'HelloWorld" (새로운 문자열 생성)
print(len(str_3))  # 10