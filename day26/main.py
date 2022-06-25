student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

# Looping through dictionaries:
# for (key, value) in student_dict.items():
#     # Access key and value
#     pass

# student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     # Access index and row
#     # Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

import pandas

nato_source = pandas.read_csv("nato_phonetic_alphabet.csv")

def gen_nato():
    nato = {row.letter: row.code for (index, row) in nato_source.iterrows()}
    return nato


def get_nato(nato_alpha, letter):
    if letter != " ":
        return nato_alpha[letter.upper()]
    else:
        return " "


def take_input():
    word = input("Enter a word to present as NATO alphabet: ")
    return word


def main():
    nato = gen_nato()
    word = take_input()
    final = [get_nato(nato, letter) for letter in word]
    print(final)


if __name__ == "__main__":
    main()
