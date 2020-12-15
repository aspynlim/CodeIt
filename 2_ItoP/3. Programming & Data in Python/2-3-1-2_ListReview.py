########## 01. 리스트에서 값의 존재 확인하기 ##########
def in_list(some_list, value):
    i = 0
    while i < len(some_list):
        if some_list[i] == value:
            return True
        i += 1
    return False

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
print(in_list(primes, 7))
print(in_list(primes, 10))

print(7 in primes)
print(10 in primes)

print(7 not in primes)
print(10 not in primes)


########## 02. Nested List ##########
grades = [[62, 75, 77], [78, 81, 86], [85, 91, 89]]
print((grades[0][0] + grades[1][0] + grades[2][0]) / 3)


########## 03. sort() Method ##########
numbers = [1, 100, 20, -1]
numbers.sort()
print(numbers)  # [-1, 1, 20, 100]


########## 04. reverse() Method ##########
numbers.reverse()
print(numbers)  # [100, 20, 1, -1]


########## 05. index() Method ##########
print(numbers[0])  # 100


########## 06. remove() Method ##########
#some_list.remove(x)는some_list에서 첫 번째로 x의 값을 갖고 있는 원소를 삭제해줍니다.
colors = ["red", "blue", "green", "blue", "red"]
colors.remove("blue")
print(colors)  # ['red', 'green', 'blue', 'red']