from stats import get_book_text, get_num_words, get_character_count, dict_to_list, report, Count

#get_character_count(get_book_text('books/frankenstein.txt'))
#get_num_words(get_book_text('books/frankenstein.txt'))

#sort_dictionary(
#    get_num_words(get_book_text('books/frankenstein.txt')), 
#    get_character_count(get_book_text('books/frankenstein.txt'))
#    )


book_text = get_book_text('books/frankenstein.txt')
num_words = get_num_words(book_text)
character_count = get_character_count(book_text)
#print(character_count)
list_words = dict_to_list(character_count)

report(num_words, list_words)