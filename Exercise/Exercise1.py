def find_numbers(start, end):
    result = []
    for i in range(start, end + 1):
        if i % 7 == 0 and i % 5 != 0:
            result.append(i)
    return result

print(find_numbers(100, 200))