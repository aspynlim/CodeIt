# def get_square(x):
#     return x * x

# y = get_square(3) + get_square(5)
# print(y)

def is_evenly_visible(number):
    return number % 2 == 0

input_num = int(input("Enter a number: "))

print(is_evenly_visible(input_num))