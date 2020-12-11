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