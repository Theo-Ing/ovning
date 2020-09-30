def txt_to_list(txt):
    with open(txt, encoding="utf8") as text:
        textString = text.read()
        return textString.split(sep="\n")

def txt_to_list_alt(txt):
    with open(txt, encoding="utf8") as text:
        a = []
        for l in text:
            a.append(l.strip())
        return a

print(txt_to_list_alt("text.txt"))