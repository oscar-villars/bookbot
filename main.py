def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def word_counter(text): 
    return len(text.split())

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_book_text(text)
    print(f"Found {num_words} total words")

main()
