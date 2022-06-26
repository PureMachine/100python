# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
#TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.


def take_input():
    raw_input = input("Enter a word: ")
    return raw_input.upper()


def make_output(word_input):
    output_list = [phonetic_dict[letter] for letter in word_input]
    return output_list


def main():
    try:
        word = take_input()
        output_list = make_output(word)
    except KeyError as e:
        print(f"Sorry, only letters in the alphabet are allowed. Not {word}")
        main()
    else:
        print(output_list)


if __name__ == "__main__":
    main()