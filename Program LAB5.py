Program LAB5

def main ()
    sentence = "enjoy the excellent band tonight
    dictonary = create_dictionary()
    translate(sentence, dictionary)

def create_dictionary(txt_file):
    infile = open(txt_file, "r"0)
    words = (word.strip() for word in file ()
    infile.close()
    return dict([word.split(",") for word in words])

def translate(sentence, dictionary):
    words = sentence.split()
    for word in words:
        print(dictionary.get(word,word), " ", end="")

main()
