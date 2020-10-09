from text_from_file import *

def longest_word(text):
    text = text + " "
    max_word = ""
    current_word = ""
    for letter in text:
        if letter.isalpha():
            current_word += letter
        else:
            if len(current_word) > len(max_word):
                max_word = current_word
            current_word = ""
    return max_word

def main():
    a = txt_to_string("text_fil.txt")
    print(longest_word(a))


if __name__ == '__main__':
    main()