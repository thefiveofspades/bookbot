def get_num_words(book_string):
    return len(book_string.split())

def character_count(book_string):
    char_dict = {}
    book_string = book_string.lower()
    for char in book_string:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] =1
    return char_dict

def character_sort(characters):
    list_dict = []
    for item in characters:
        list_dict.append({"name": item, "num": characters[item]})
    list_dict.sort(reverse=True, key=sort_on)
    return list_dict

def sort_on(dict):
    return dict["num"]