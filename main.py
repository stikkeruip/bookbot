from stats import get_num_words, get_char_count, get_sorted_chars
import sys

def get_book_text(file_path):
    return open(file_path).read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_name = sys.argv[1]
    book_text = get_book_text(file_name)

    num_words = get_num_words(book_text)

    char_counts = get_char_count(book_text)  # str → dict
    sorted_chars = get_sorted_chars(char_counts)  # dict → sorted list

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_name}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char, count in sorted_chars:
        if char.isalpha():
            print(f"{char}: {count}")

main()