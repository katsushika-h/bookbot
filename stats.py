def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents


def get_num_words(text):
    split_words = text.split()
    print(str(len(split_words)) +" words found in the document")
    return len(split_words)

def get_character_count(text):
    symbol_dict = {}
    text = text.lower()

    for character in text:
        if not character in symbol_dict:
            symbol_dict[character] = 1
        else:
            symbol_dict[character] += 1
    return symbol_dict

def Count(number):
    return number['Count']

def dict_to_list(dict):
    list = []
    for item in dict:
        list.append({"Character":item, "Count":dict[item]})
    
    list.sort(key=Count, reverse=True)
    #print(list)
    return(list)
    


def report(word_count, character_dict, path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in character_dict:
        print(f"{item['Character']}: {item['Count']}")
    
    print("============= END ===============")


