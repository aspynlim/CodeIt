# Dictionary : key-value pair

my_dictionary = {
    'a': 25,
    'b': 10
}
my_dictionary['c'] = -20

print(type(my_dictionary))     # <class 'dict'>

print(my_dictionary)           # {'a': 25, 'b': 10, 'c': -20}

print(my_dictionary.values())  # dict_values([25, 10, -20])

print(25 in my_dictionary.values())  # True

for key, value in my_dictionary.items():
    print(f'{key}: {value}')
# a: 25
# b: 10
# c: -20

print(len(my_dictionary))  # 3

print(259 not in my_dictionary.values())
