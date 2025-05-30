import sys
from stats import get_num_words
from stats import character_count
from stats import character_sort

def main(bookpath):
    book = get_book_text(bookpath)
    word_count = get_num_words(book)
    characters = character_count(book)
    dict_list = character_sort(characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {bookpath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in dict_list:
        if item["name"].isalpha():
            print(f'{item["name"]}: {item["num"]}')
    print("============= END ===============")

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
main(sys.argv[1])