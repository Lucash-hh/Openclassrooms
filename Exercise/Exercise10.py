def binary_divisible_by_5(inputbinary):
    binary_list = inputbinary.split(',')
    divisible = []
    for b in binary_list:
        if int(b, 2)% 5 == 0:
            divisible.append(b)
    return divisible
            

inputbinary = "1111,1111,1111,1001"
print(binary_divisible_by_5(inputbinary))
