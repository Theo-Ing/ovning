def max_word_length(text):
    text = text + " "
    max_length = 0
    current_length = 0
    for letter in text:
        if letter.isalpha():
            current_length += 1
        else:
            if current_length > max_length:
                max_length = current_length
            current_length = 0
    return max_length

def main():
    a = input("Skriv din text: ")
    print(max_word_length(a))


if __name__ == '__main__':
    main()