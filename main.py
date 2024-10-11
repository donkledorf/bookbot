def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    print(f"The book contains {word_count} words.")
    character_count = count_characters(text)
    print(character_count)
    


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

        


main()
