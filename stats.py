def count_words(text):
    words = text.split()
    return len(words)

def letter_count(text):
    text = text.lower()
    count = {}
    for letter in text:
        count[letter] = 0
    for letter in text:
        count[letter] += 1
    return count

def dict_sort(count_dict):
    for letter in count_dict:
        num = count_dict[letter]
        if letter.isalpha():
            print(f"{letter}: {num}")