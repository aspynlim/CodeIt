with open('2_ItoP/4_Python_Module/data/vocabulary2.txt', 'a', encoding='UTF-8') as f:
    while True:
        original_word = input('영어 단어를 입력하세요: ')
        translated_word = input('한국어 뜻을 입력하세요: ')

        if original_word == 'q' or translated_word == 'q':
            break
        else:
            f.write(f'{original_word}: {translated_word}\n')

