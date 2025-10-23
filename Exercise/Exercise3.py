def convert_input_to_list_and_tuple(string):
    value = string.split(",")
    return value, tuple(value)

print(convert_input_to_list_and_tuple("3,6,5,3,2,8"))
