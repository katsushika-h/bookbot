def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents


def get_num_words(text):
    split_words = text.split()
    print(str(len(split_words)) +" words found in the document")
