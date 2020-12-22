with open('2_ItoP/4_Python_Module/data/chicken2.txt', 'r', encoding='UTF-8') as f:
    total_revenue = 0
    total_days = 0
        
    for line in f:
        data = line.strip().split('일: ')
        total_revenue += int(data[1])
        total_days += 1
    
    print(total_revenue / total_days)


