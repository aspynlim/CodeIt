# 1. 'q'가 아닌 이상 loop을 돌면서 한 번은 영어, 한번은 한국어 뜻을 받는다.
# 2. 받으면 {영어: 한국어} 형태로 loop을 돌면서 입력시킨다.

temp_dict = {}

while True:
    key_temp = input('영어 단어를 입력하세요: ')
    temp_value = input('한국어 뜻을 입력하세요: ')
    if key_temp == 'q' or temp_value == 'q':
        break
    else:
        temp_dict[key_temp] = temp_value

print(temp_dict)

with open('2_ItoP/4_Python_Module/data/vocabulary.txt', 'a', encoding='UTF8') as f:
    for pair in temp_dict:
        f.write(f'{pair}: {temp_dict[pair]}\n')

