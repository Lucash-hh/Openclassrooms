def catch_zero_division():
    try:
        return 10 / 0
    except ZeroDivisionError:
        print("Zero divison error")

catch_zero_division()