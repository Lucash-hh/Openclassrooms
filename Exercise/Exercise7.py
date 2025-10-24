def sort_words(string):
    words = string.split(',')
    words.sort()
    return words

print(sort_words("potato,avocado,berry"))