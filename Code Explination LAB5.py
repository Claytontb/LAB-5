Code Explination LAB5

"""
The program is trying to translate a sentence captured as user input.
We first read in the text file textese.txt.
then from the text file, we create a list of strings from each lines in the text file.
Then, we crere a dictionary the list.
Once the text file has been read into memory, we close the file.

We then define a function for translating which envolves splitting the user input (sentence) into an 
array of strings ("enjoy the excellent band tonight") ["enjoy", "the", "excellent", "band", "tonight"]

once we have the array of strings representing the users input sentence, we
loop through each words, find the key matching the word and return back to the value tied to the word
in our dictionary.

Print out the translated sentence to the user
"""

"""
main()
    set sentence = input()
    set dictionary = create_dictionary()
    translate(sentence, dictionary)

translate(sentence, dictionary):
    words = for each of the word in the sentence 
    for the words, translate the word 
    print translated sentence to user

create_dictionary()
    read in textese.txt 
    create list = each line from the file 
    close the file 
    create a dict off of the list 
    return to dict 

    main()
"""
# program is translating the sentence enjoy the band tonight and categorizing the sentense into a dictionary standard 
def main ()
    sentence = "enjoy the excellent band tonight
    dictonary = create_dictionary()
    translate(sentence, dictionary)

#program is creating a dictionary base of the given words of a text file, and splitting and categorizing the txt files words
def create_dictionary(txt_file):
    infile = open(txt_file, "r"0)
    words = (word.strip() for word in file ()
    infile.close()
    return dict([word.split(",") for word in words])

#program is translating the words to the dictionary and finalizing the diffrent words to appear in the diffrent catregories 
def translate(sentence, dictionary):
    words = sentence.split()
    for word in words:
        print(dictionary.get(word,word), " ", end="")

main()