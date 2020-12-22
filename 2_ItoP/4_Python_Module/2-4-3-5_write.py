# with open('2_ItoP/4_Python_Module/data/new_file.txt', 'w', encoding='UTF8') as f:
#     f.write('Hello World\n')
#     f.write('Hello World')

# 파일이 없으면 새로 만드므로 'w'(write) 대신 'a'(append)를 써도 됨
with open('2_ItoP/4_Python_Module/data/new_file.txt', 'a', encoding='UTF8') as f:
    f.write('Hello TEST\n')
    f.write('Hello TEST')