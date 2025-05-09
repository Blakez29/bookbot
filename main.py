from stats import count_words, letter_count, dict_sort
import sys

def get_book_text(text):
    with open(text) as f:
        contents = f.read()
    return contents

def main():
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found in {path}...")
    print("----------- Word Count ----------")
    text = get_book_text(path)
    count = count_words(text)
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    count_dict = letter_count(text)
    dict_sort(count_dict)
    print("============= END ===============")

main()
