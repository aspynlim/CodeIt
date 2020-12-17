def mask_security_number(ssn_num):
    return ssn_num[:-4] + '****'

print(mask_security_number("880720-1234567"))
print(mask_security_number("8807201234567"))


def mask_security_number2(ssn_num):
    ssn_num_list = list(ssn_num)

    for i in range(len(ssn_num_list) -4, len(ssn_num_list)):
        ssn_num_list[i] = '*'
    
    return ''.join(ssn_num_list)

print(mask_security_number2("880720-1234567"))
print(mask_security_number2("8807201234567"))