import os

files = [f for f in os.listdir('./2_ItoP/4_Python_Module/data')]
for f in files:
    print(f)  # chicken.txt

with open('2_ItoP/4_Python_Module/data/chicken.txt', 'r', encoding='UTF8') as f:
    for line in f:
        print(line)