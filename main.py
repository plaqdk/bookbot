from stats import count_char, count_words, sort_char
import sys

if len(sys.argv) != 2:
    print(f"Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book = sys.argv[1] 

def get_book_text():
    with open(book) as f:
        file_content = f.read()
    return file_content


def main():
    count_char(get_book_text())
    
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print(f"----------- Word Count ----------")
    print(f"Found {count_words(get_book_text())} total words")
    print(f"--------- Character Count -------")
    for d in sort_char(count_char(get_book_text())):
        print(f"{d['char']}: {d['num']}")

    print(f"============= END ===============")

main()
