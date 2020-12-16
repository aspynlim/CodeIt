def reverse_dict(dict):
    new_dict = {}
    for key, value in dict.items():
        new_dict[value] = key
    return new_dict

vocab = {
    'first': 'apple',
    'second': 'pineapple',
    'third': 'peach'
}

print(f'{vocab}')
# {'first': 'apple', 'second': 'pineapple', 'third': 'peach'}

reverse_vocab = reverse_dict(vocab)
print(f'{reverse_vocab}')
# {'apple': 'first', 'pineapple': 'second', 'peach': 'third'}

