from stats import get_num_words, get_char_count, get_sorted_chars

def get_book_text(file_path):
    return open(file_path).read()

def main():
    file_name = 'books/frankenstein.txt'
    book_text = get_book_text(file_name)

    num_words = get_num_words(book_text)

    char_counts = get_char_count(book_text)  # str → dict
    sorted_chars = get_sorted_chars(char_counts)  # dict → sorted list

    print(sorted_chars)


main()