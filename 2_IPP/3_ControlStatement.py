########## 01. While ##########
i = 1
while i <= 3:
    print(f'hello {i}')
    i += 1

# hello 1
# hello 2
# hello 3


########## 02. While QUIZ 1 ##########
i = 2
while i >= 100:
    i += 1
    if(i % 23 == 0):
        print(i)
        break
# 2 ~ 100 : 2의 배수 출력


########## 03. If QUIZ 1 ##########
def print_grade(midterm_score, final_score):
    total = midterm_score + final_score
    if total >= 90:
        print("A")
    elif total >= 80:
        print("B")
    elif total >= 70:
        print("C")
    elif total >= 60:
        print("D")
    else:
        print("F")
        
# 테스트
print_grade(40, 45)  # B
print_grade(20, 35)  # F
print_grade(30, 32)  # D
print_grade(50, 45)  # A


########## 03. If QUIZ 2 ##########
# while문과 if문을 활용하여, 100 이하의 자연수 중 8의 배수이지만 12의 배수는 아닌 것을 모두 출력하세요.

i = 1
while i <= 100:
    if i % 8 == 0 and i % 12 != 0:
        print(i)
    i += 1


########## 04. If QUIZ 3 ##########
# 10보다 작은 2 또는 3의 배수는 2, 3, 4, 6, 8, 9이며, 이들의 합은 32입니다.
# while문과 if문을 활용하여, 1,000보다 작은 자연수 중 2 또는 3의 배수의 합을 출력하는 프로그램을 써 보세요.

i = 1
limit = 10
sum = 0

while i < limit:
    if i % 2 == 0 or i % 3 == 0:
        sum += i
    i += 1

print(sum)  # 32


########## 04. If QUIZ 4 ##########
# 정수 n의 약수는 n을 나누었을 때 나누어 떨어지는 수입니다. 만약 정수 i가 정수 n의 약수라면, n을 i로 나누었을 때 나머지가 0이 나와야 하는 거죠.
# 정수 120의 약수를 모두 출력하고, 총 몇개의 약수가 있는지 출력하는 프로그램을 써 보세요. 

number = 120
total_math_factors = 0
i = 1

while i <= number:
    if number % i == 0:
        print(i)
        total_math_factors += 1
    i += 1

print(f"{number}의 약수는 총 {total_math_factors}개입니다.")


########## 04. If QUIZ 5 ##########
# 1988년 쌍문동에 사는 택이는 바둑 대회 우승 상금으로 5,000만원을 받았습니다. 하지만 바둑 외에는 아는 게 없으니, 이웃 어른들에게 이 돈으로 무엇을 해야 할지 물어보기로 하였습니다.
# 은행에서 근무하는 동일 아저씨는 은행에 돈을 맡겨서 매년 이자로 12%씩 받는 것을 추천하셨습니다. 1년 후인 1989년에는 5,000만원의 12% 이자인 600만원이 더해져 5,600만원이 된다고 하면서요.
# 이 이야기를 들은 미란 아주머니는 고작 12% 때문에 생돈을 은행에 넣느냐며, 얼마 전 지어진 은마아파트를 사라고 추천하셨습니다. 당시 은마아파트의 매매가는 5,000만원이었죠.
# 2016년 기준 은마아파트의 매매가는 11억원인데요. 1988년 은행에 5,000만원을 넣었을 경우 2016년에는 얼마가 있을지 계산하여, 동일 아저씨와 미란 아주머니 중 누구의 말을 듣는 것이 좋았을지 판단해 보세요. 

INTEREST_RATE = 0.12
APT_PRICE_2016 = 1100000000

award_money = 50000000
current_year = 2016
investment_year = 1988
years = current_year - investment_year

i = 1
while i <= years:
    award_money = award_money * (1 + INTEREST_RATE)
    i += 1

if APT_PRICE_2016 > award_money:
    print(f"{int(APT_PRICE_2016 - award_money)}원 차이로 미란 아주머니 말씀이 맞습니다.")
else:
    print(f"{int(award_money - APT_PRICE_2016)}원 차이로 동일 아저씨 말씀이 맞습니다.")