from stats import get_num_char, get_num_words
import sys

argv_num = len(sys.argv)
if 1 < argv_num < 3:
    path = sys.argv[1]
else:
    print('Usage: python3 main.py <path_to_book>')
    sys.exit(1)

#Usage: python3 main.py <path_to_book>

def main():
    word_count = get_num_words(path)
    char_count = get_num_char(path)

    print_report(word_count, char_count)



def print_report(word_count, chars):
    #print report
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {path}...')
    print('----------- Word Count ----------')
    print(f"Found {word_count} total words")
    print('--------- Character Count -------')
    for char in chars:
        if char['char'].isalpha() :
            print(f'{char['char']}: {char['num']}')
    print('============= END ===============')

    return
    

main()
