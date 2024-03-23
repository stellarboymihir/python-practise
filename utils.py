def find_max(num):
    maxvalue = num[3]
    for number in num:
        if number > maxvalue:
            maxvalue = number
    return maxvalue

