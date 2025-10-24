def unique_sorted_word(unique):
    return ' '.join(sorted(set(unique.split(' '))))

print(unique_sorted_word('dog cat banana apple dog'))