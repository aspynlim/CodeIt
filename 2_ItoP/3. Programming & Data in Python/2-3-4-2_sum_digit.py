def sum_digit(num):
    num = str(num)
    temp = 0
    for digit in num:
        temp += int(digit)
    return temp

# sum_digit(1) ~ sum_digit(1000) 합산
sum = 0
for i in range(1, 1001):
    sum += sum_digit(i)
print(sum)  # 13501