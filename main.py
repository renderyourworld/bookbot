def get_book_contents(path):
    with open(path) as f:
        return f.read()

def get_book_words(text):
    words = text.split()
    
    return len(words)

def get_character_count(text):
    chars_dict = {}
    for c in text:
        c_lower = c.lower()
        if c_lower in chars_dict:
            chars_dict[c_lower] += 1
        else:
            chars_dict[c_lower] = 1

    return chars_dict

def convert_dict_to_sorted_list(chars_dict):
    sorted_list = []
    for c in chars_dict:
        if c.isalpha():
            sorted_list.append({"name": c, "num": chars_dict[c]})

    sorted_list.sort(reverse=True, key=lambda x: x['num'])

    return sorted_list
    
def print_report(book_path, words, chars_dict):
    print(f"--- Begin report of {book_path} ---")
    print(f"{words} words found in the document")
    print()

    char_list = convert_dict_to_sorted_list(chars_dict)
    for c in char_list:
        print(f"The '{c['name']}' character was found {c['num']} times")
    print("--- End report ---")

        

def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_contents(book_path)
    words = get_book_words(book_text)
    chars_dict = get_character_count(book_text)

    print_report(book_path, words, chars_dict)


main()