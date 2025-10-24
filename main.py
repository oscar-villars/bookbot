from stats import word_counter, chars_dict_sorted, character_counter
import sys


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
   
    num_words = word_counter(text)
    print(f"Found {num_words} total words")

    chars = character_counter(text)
    sorted_chars = chars_dict_sorted(chars)

    for item in sorted_chars: 
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")

main()
