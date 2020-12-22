with open('2_ItoP/4_Python_Module/data/vocabulary.txt', 'r', encoding='UTF8') as f:
    for line in f:
        word = line.strip().split(': ')[1]
        answer = line.strip().split(': ')[0]
        guess = input(f'{word}: ')

        if guess == answer:
            print('맞았습니다!')
        else:
            print(f'아쉽습니다. 정답은 {answer} 입니다.')