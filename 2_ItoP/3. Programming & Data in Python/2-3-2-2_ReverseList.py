########## 05. 실습과제 IV ##########
numbers1 = (1, 2)
print(type(numbers1))  # Class 'tuple'
numbers2 = 1, 2
print(type(numbers2))  # Class 'tuple'


# numbers라는 리스트가 주어졌을 때, for문을 사용하여 리스트를 거꾸로 뒤집어 보세요!

# Method 1
numbers = [2, 3, 5, 7, 11, 13, 17, 19]

for left in range(int(len(numbers) / 2)):
    right = len(numbers) - left - 1
    numbers[right], numbers[left] = numbers[left], numbers[right]

print("뒤집어진 리스트: " + str(numbers))

# Method 2
numbers2 = [2, 3, 5, 7, 11, 13, 17, 19]

for left in range(int(len(numbers2) / 2)):
    right = len(numbers2) - left - 1
    temp = numbers2[left]
    numbers2[left] = numbers2[right]
    numbers2[right] = temp

print("뒤집어진 리스트: " + str(numbers2))