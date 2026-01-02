def get_num_words(book_text):
    return len(book_text.split())

def get_char_count(book_text):
    book_text = book_text.lower()
    chars = {}

    for char in book_text:
        chars[char] = chars.get(char, 0) + 1

    return chars

def get_sorted_chars(char_dict):
    return sorted(char_dict.items(), key=lambda x: x[1], reverse=True)