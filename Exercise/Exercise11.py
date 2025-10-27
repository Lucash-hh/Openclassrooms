def even_digit_numbers(start, end):
    even = []

    for n in range(start, end + 1):
        all_even = True

        for digit in str(n):
            if int(digit) % 2 != 0:
                all_even = False
                break
        
        if all_even:
            even.append(str(n))
    
    print(",".join(even))

even_digit_numbers(1200,2010)