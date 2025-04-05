from stats import word_count, character_count, sorted_list
import sys

def main():
    if not len(sys.argv) == 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = word_count(text)
    counts = character_count(text)
    chars_sorted_list = sorted_list(counts)
    print_report(book_path, num_words, chars_sorted_list)

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()
    
def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in chars_sorted_list:
        if not i["char"].isalpha():
            continue
        print(f"{i["char"]}: {i["count"]}")
    print("============= END ===============")
    
main()