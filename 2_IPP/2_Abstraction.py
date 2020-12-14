##########  01. Function ##########
def square(x):
    return x * x

print("Before a function is called")
print(square(3) + square(4))           #25
print("After a function is called")


##########  02. Return ##########
def print_square(x):
    print(x * x)

def get_square(x):
    return x * x

print_square(3)                          # 9
get_square(3)                            # 9
print(f"3 x 3 is {print_square(3)}.")    # 3 x 3 is None.
print(f"3 x 3 is {get_square(3)}.")      # 3 x 3 is 9.


########## 03. Optional Parameter ##########
def myself(name, age, nationality="Korea"):
    print(f"My name is {name} & {age} years old. And, I'm from {nationality}.")

myself("Jane", 15)             # My name is Jane & 15 years old. And, I'm from Korea.
myself("Kyle", 20, "Canada")   # My name is Kyle & 20 years old. And, I'm from Canada.


########## Abstraction 퀴즈 I ##########
def hello(name):
    print(f"Hello, my name is {name}.")
    return "Nice to meet you!" # Dead Code

print(hello("Kyle"))           # Hello, my name is Kyle.
                               # Nice to meet you!
hello("Jo")                    # Hello, my name is Jo.


########## 04. Scope ##########
x = 20

def my_function():
    x = 3
    print(x)

my_function()  # 3
print(x)       # 20


########## Scope 퀴즈 I ##########
def test():
    y = 2
    y = 100

test()       # Nothing is printed.
#print(y)     # NameError: name 'y' is not defined


########## 05. 상수(Constant) ##########
PI = 3.14   # 다 대문자로 표시, A value that is not expected to be changed.

def calculate_area(r):
    return PI * r * r

radius = 4
print(f"When the radius {radius}, the calculated area is {calculate_area(radius)}.")
# When the radius 4, the calculated area is 50.24.


########## 06. Abstraction Quiz I ##########
def is_evenly_divisible(number):
    return number % 2 == 0

print(is_evenly_divisible(3))   # False
print(is_evenly_divisible(10))  # True


def is_evenly_divisible_2(number):
    return bool(not number % 2)

print(is_evenly_divisible_2(3))   # False
print(is_evenly_divisible_2(10))  # True


########## 07. Abstraction Quiz I ##########
def calculate_change(payment, cost):
    change = payment - cost
    fifty_thousand_won = 50000
    ten_thousand_won = 10000
    five_thousand_won = 5000
    one_thousand_won = 1000
    
    fifty_count = change // fifty_thousand_won
    ten_count = (change % fifty_thousand_won) // ten_thousand_won
    five_count = (change % ten_thousand_won) // five_thousand_won
    one_count = (change % five_thousand_won) // one_thousand_won

    print(f"50000원 지폐: {fifty_count}장")
    print(f"10000원 지폐: {ten_count}장")
    print(f"5000원 지폐: {five_count}장")
    print(f"1000원 지폐: {one_count}장")


# 테스트
calculate_change(100000, 33000)
print()
calculate_change(500000, 378000)