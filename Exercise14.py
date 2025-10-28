def sum_of_series(a):
    return sum(int(str(a) * i) for i in range(1, 5))
    
print(sum_of_series(7))