########## 01. for Method ##########
numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
# The enumerate() function assigns an index to each item in an iterable object that can be used to reference the item later. 
for i, item in enumerate(numbers, start=0):
    print(i, item)

for i in range(len(numbers)):
    print(i, numbers[i])


########## 02. 실습과제 I ##########
for i in range(11):
    print(f"2^{i} = {2 ** i}")


########## 03. 실습과제 II ##########
for left in range(1, 10):
    for right in range (1, 10):
        print(f"{left} * {right} = {left * right}")

########## 04. 실습과제 III ##########
# a + b + c = 1000
# a < b < c
# a^2 + b^2 = c^2

for a in range(1, 1000):
    for b in range(1, 1000):
        c = 1000 - a - b
        if a * a + b * b == c * c and a < b < c:
            print(a * b * c)