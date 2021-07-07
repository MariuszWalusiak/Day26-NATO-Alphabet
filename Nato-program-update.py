import pandas


#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
df = pandas.read_csv("nato_phonetic_alphabet.csv")
letters_dictionary = {row.letter: row.code for (index, row) in df.iterrows()}



#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

def generate_phonetic():
    name = input("Enter a word: ").upper()
    try:
        output_list = [letters_dictionary[letter] for letter in name]
    except KeyError:
        print("Sorry, only letters in the alphabet")
        generate_phonetic()
    else:
        print(output_list)

generate_phonetic()