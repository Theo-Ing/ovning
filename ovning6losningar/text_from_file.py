def txt_to_string(txt):
    with open(txt, encoding="utf8") as f:
        text = f.read()
        text = text.replace("\n", " ")
        text = text.replace("\t", " ")
    return text

if __name__ == '__main__':
    print("This is a module, please do not run as main")