def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"The book contains {word_count} words.")
    character_count = count_characters(text)
    char_list = [{'char': char, 'count': count} for char, count in character_count.items()]
    char_list.sort(reverse=True, key=sort_on)
    for item in char_list:
        print(f"the '{item['char']}' was found {item['count']} times")
    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()


def count_words(text):
   word = text.split()
   return len(word)


def count_characters(text):
    characters = {}
    for char in text.lower():
        if char.isalpha():
           characters[char] = characters.get(char, 0) + 1
    return characters

        
def sort_on(dict_item):
    return dict_item['count']

main()
