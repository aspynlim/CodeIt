with open('2_ItoP/4_Python_Module/data/chicken2.txt', 'r', encoding='UTF8') as f:
    result = []
    for line in f:
        # print(line.strip().split('일: '))
        sales_record = line.strip().split('일: ')
        result.append(sales_record)
    total_days = len(result)
    print(total_days)  # 31

    sum = 0
    for i in result:
        sum += int(i[1])
    print(sum)  # 15559400
    print(sum / total_days)  # 501916.12903225806


    