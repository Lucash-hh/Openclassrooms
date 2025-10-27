def count_case(case):
    dict = {'UPPER CASE' : 0, 'LOWER CASE': 0,}
    for c in str(case):
        if c.isupper():
            dict['UPPER CASE'] += 1
        elif c.islower():
            dict['LOWER CASE'] += 1
    return dict

print(count_case("Hello World"))