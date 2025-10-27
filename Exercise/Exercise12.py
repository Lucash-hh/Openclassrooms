def count_letters_digits_dict(ldig):
    let_dig = {}
    let = []
    dig = []
    for l in str(ldig):
        if l.isalpha():
            let.append(l)
            let_dig["Letters"] = len(let)

    for d in str(ldig):
        if d.isdigit():
            dig.append(d)
            let_dig["Digits"] = len(dig)

    return let_dig

print(count_letters_digits_dict("Data123 Science 2025"))