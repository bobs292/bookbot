import sys
if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
book_path = sys.argv[1]

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()
        

def main():
    file_contents = get_book_text(book_path)
    from stats import get_num_words
    from stats import get_count_Letters
    from stats import sort
    count = get_count_Letters(file_contents)
    number = get_num_words(file_contents)
    sorted = sort(count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {number} total words")
    print("--------- Character Count -------")
    for key, value in sorted.items():
        if key.isalpha():
            print(f"{key}: {value}")
    print("============= END ===============")
main()