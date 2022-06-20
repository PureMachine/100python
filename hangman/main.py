from ast import Return
from curses.ascii import isalpha
from dis import dis
import random

def random_word(word_list):
    chosen_word_index = random.randrange(0,(len(word_list)))
    return word_list[chosen_word_index]

def user_input():
    raw_in = input("Guess a letter from the alphabet: ")
    if raw_in:
        if isalpha(raw_in):
            return raw_in.lower()
    else:
        return ("a")

def compare_word(guess, chosen, board):
    outcome = False
    if guess in chosen:
        for i, letter in enumerate(chosen):
            if letter == guess:
                board[i] = letter
                outcome = True                
    else:
        print("No match found")
    return board, outcome

def generate_display(chosen_word):
    display = []
    for _letter in chosen_word:
        display.append("_")
    return display

def main():
    word_list = ["farnz","bary","berry", "firehouse", "replica"]
    chosen_word = random_word(word_list)
    board = generate_display(chosen_word)
    lives = 3
    correct = 0
    already_chosen = []
    while lives > 0 and correct < len(chosen_word):
        guess = user_input()
        board, state = compare_word(guess, chosen_word, board)
        if state and guess not in already_chosen:
            correct += 1
            already_chosen.append(guess)
        elif state:
            print("You have already chosen that letter")
        else:
            lives -= 1
        print(board)

    print(lives, correct)
    if lives == 0:
        print("You lose")
    
    if correct == len(chosen_word):
        print("You win")

if __name__ == "__main__":
    main()
