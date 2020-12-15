########## 01. List ##########
numbers = [10, 20, 30, 40, 50]

print(numbers[0])   # 10
print(numbers[-1])  # 50


########## 02. List Slicing ##########
print(numbers[0:3]) # [10, 20, 30]
print(numbers[:3]) # [10, 20, 30]


########## 03. List Function ##########
fruits = ["A", "B", "C"]
fruits.append("apple")
del fruits[1]
print(fruits)                       # ['A', 'C', 'apple']
print(len(fruits))                  # 4

fruits.insert(0, "strawberry")
fruits.extend(["grape", "cherry"])  # ['strawberry', 'A', 'C', 'D', 'grape', 'cherry']
print(fruits)


########## 04. List 정렬 ##########
orders = [19, 13, 2, 5, 3, 11, 7, 17]
orders_list = sorted(orders)  # 기존 리스트 안 건드림 / return 
reversed_orders_list = sorted(orders, reverse=True)

print(orders_list)            # [2, 3, 5, 7, 11, 13, 17, 19]
print(reversed_orders_list)   # [19, 17, 13, 11, 7, 5, 3, 2]
print(orders)                 # [19, 13, 2, 5, 3, 11, 7, 17] 


orders_list_2 = orders.sort() # 기존 리스트 정렬 / return 안 함
print(orders_list_2)          # None
print(orders)                 # [2, 3, 5, 7, 11, 13, 17, 19]

orders.sort(reverse=True)
print(orders)                 # [19, 17, 13, 11, 7, 5, 3, 2] 


########## 05. 실습과제 I ##########
greetings = ["안녕", "니하오", "곤니찌와", "올라", "싸와디캅", "헬로", "봉주르"]

i = 0
while i < len(greetings):
    print(greetings[i])
    i += 1


########## 05. 실습과제 II ##########
def fahrenheit_to_celsius(fahrenheit):
    i = 0
    while i < len(fahrenheit):
        # Limiting floats to one decimal point
        fahrenheit[i] = ((fahrenheit[i] - 32) * 5) / 9
        fahrenheit[i] = round(fahrenheit[i], 1)
        i += 1

temperature_list = [40, 15, 32, 64, -4, 11]
print("화씨 온도 리스트: " + str(temperature_list))  # 화씨 온도 출력

fahrenheit_to_celsius(temperature_list)
print("섭씨 온도 리스트: " + str(temperature_list))  # 섭씨 온도 출력


########## 06. 실습과제 III ##########
# 원화(￦)에서 달러($)로 변환하는 함수
def krw_to_usd(krw):
    i = 0
    while i < len(krw):
        krw[i] = round((krw[i] / 1000), 1)
        i += 1

# 달러($)에서 엔화(￥)로 변환하는 함수
def usd_to_jpy(usd):
    j = 0
    while j < len(usd):
        usd[j] = round(((usd[j] * 1000) / 8), 1)
        j += 1

# 원화(￦)으로 각각 얼마인가요?
amounts = [34000, 13000, 5000, 21000, 1000, 2000, 8000, 3000]
print("한국 화폐: " + str(amounts))
 
# amounts를 원화(￦)에서 달러($)로 변환하기
krw_to_usd(amounts)
print("미국 화폐: " + str(amounts))

# amounts를 달러($)에서 엔화(￥)으로 변환하기
usd_to_jpy(amounts)
print("일본 화폐: " + str(amounts))


########## 07. 실습과제 IV ##########
# 빈 리스트 만들기
numbers_list = []
print(numbers_list)

# numbers_list에 값들 추가
temp = [1, 7, 3, 6, 5, 2, 13, 14]
i = 0
while i < len(temp):
    numbers_list.append(temp[i])
    i += 1
print(numbers_list)

# numbers_list에서 홀수 제거
i = 0
while i < len(numbers_list):
    while numbers_list[i] % 2 == 1:
        del numbers_list[i]
        continue
    i += 1
print(numbers_list)

# numbers_list의 인덱스 0 자리에 20이라는 값 삽입
numbers_list.insert(0, 20)
print(numbers_list)

# numbers_list를 정렬해서 출력
numbers_list.sort()
print(numbers_list)
