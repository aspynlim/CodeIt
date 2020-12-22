import random

with open('2_ItoP/4_Python_Module/data/vocabulary.txt', 'r', encoding='UTF8') as f:
    vocab = {}
    for line in f:
        key = line.strip().split(': ')[0]
        value = line.strip().split(': ')[1]
        vocab[key] = value
    print(vocab)

    keys = list(vocab.keys())  # keys만 가져와서 리스트 만들기
    print(keys)

    while True:
        index = random.randint(0, len(keys) - 1)   # 0 ~ '리스트의 길이 - 1' 사이의 랜덤한 숫자

        english_word = keys[index]
        korean_word = vocab[english_word]
        guess = input(f'{korean_word}: ')

        if guess == 'q':
            break
        elif guess == english_word:
            print('맞았습니다!')
        else:
            print(f'아쉽습니다. 정답은 {english_word} 입니다.')

