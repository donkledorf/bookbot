def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    print(f"The book contains {word_count} words.")


def get_book_text(path):
    with open(path) as f:
        return f.read()

#I need to split the entire text and then count each individual word once i have the number i need to 
#return it as a string and print it
def count_words(text):
   word = text.split()
   return len(word)


    

main()
