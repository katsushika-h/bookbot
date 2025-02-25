from stats import (get_book_text, 
get_num_words, 
get_character_count, 
dict_to_list, report, 
Count)


import sys



try:
     sys.argv[1] 
except IndexError:
    print('Usage: python3 main.py <path_to_book>')
    sys.exit(1)



book_text = get_book_text(sys.argv[1])
num_words = get_num_words(book_text)
character_count = get_character_count(book_text)

list_words = dict_to_list(character_count)

report(num_words, list_words, sys.argv[1])