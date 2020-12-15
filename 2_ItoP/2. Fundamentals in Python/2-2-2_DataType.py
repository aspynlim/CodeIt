########## 01. 숫자형 ##########
# 나머지
print(7 % 3)    # 1

# 거듭제곱
# 소수형이 섞여 있으면 결과가 소수형으로 표현되어서 나옴
print(2.0 ** 3) # 8.0
print(2 ** 3)   # 8

# 나눗셈 (이건 정수형끼리 해도 결과가 소수형으로 나옴)
print(6 / 2)    # 3.0
print(6.0 / 2)  # 3.0


########## 02. 숫자형 심화 ##########
# Floor Division (버림 나눗셈)
print(7 // 2)    # 3
print(7.0 // 2)  # 3.0 (버리고 나서 .0 을 붙임)

# round (반올림)
print(round(3.1415926535, 3)) # 3.142


########## 03. 문자형 ##########
print("I\'m \"excited\" to\nlearn Python !") 
# I'm "excited" to
# learn Python !


########## 04. Type Conversion/Casting ##########
print(int(3.8))        # 3
print(float(3))        # 3.0
print(str(2) + str(0)) # 20


########## 자료형 퀴즈 I ##########
print(2 ** 3.0)               # 8.0
print(int("3") + float("5"))  # 8.0
print(str(4.0) * 2)           # 4.04.0
print(float(int(42 / 5)))     # 8.0
print(2 * (3 + 1))            # 8


########## 05. format을 이용한 문자열 포맷팅 ##########
year = 2021
month = "January"
day = 1
print("Today is {} {}, {}.".format(month, day, year))
# Today is January 1, 2021.

print("I like {2}, {1}, {0}!".format("blue", "yellow", "red"))

num_1 = 1
num_2 = 3
print("{0} divide by {1} is {2}.".format(num_1, num_2, num_1 / num_2))
# 1 divide by 3 is 0.3333333333333333.
print("{0} divide by {1} is {2:.2f}.".format(num_1, num_2, num_1 / num_2))
# 1 divide by 3 is 0.33.
print("{0} divide by {1} is {2:.0f}.".format(num_1, num_2, num_1 / num_2))
# 1 divide by 3 is 0.


##########  문자열 포맷팅 퀴즈 I ##########
# 5시간에 28554.0원 벌었습니다.
wage = 5 
exchange_rate = 1142.16
print(f"5시간에 {(wage * 5 * exchange_rate):.1f}원 벌었습니다.")


##########  06. Boolean ##########
# skipped


##########  06. Boolean ##########
print(type(3))       # <class 'int'>
print(type(3.0))     # <class 'float'>
print(type("True"))  # <class 'str'>
print(type(True))    # <class 'bool'>

def hello(self, parameter_list):
    print("hello")
print(type(hello))   # <class 'function'>
print(type(print))   # <class 'builtin_function_or_method'>


##########  Boolean 퀴즈 I ##########
print(((12 >= 10 and not 3 > 4) or 3 ** 2 != 9))    # True