def mask_security_number(ssn_num):
    hide_ssn = '****'

    if len(ssn_num) == 14:
        ssn_left = ssn_num[0:10]
    else:
        ssn_left = ssn_num[0:9]
    temp_tuple = (ssn_left, hide_ssn)
    return "".join(temp_tuple)

print(mask_security_number("880720-1234567"))
print(mask_security_number("8807201234567"))
print(mask_security_number("930124-7654321"))
print(mask_security_number("9301247654321"))
print(mask_security_number("761214-2357111"))
print(mask_security_number("7612142357111"))