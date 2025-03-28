import random

def read_word_bank(file_name):
    word_bank = {}
    with open(file_name, 'r') as file:
        for line in file:
            word = line.strip()
            word_bank[word] = hash(word)
    return word_bank

def remove_non_words(word_bank, guess, feedback):
    filtered_words = {}

    for word in word_bank:
        valid = True
        
        for i, letter in enumerate(guess):
            if feedback[i] == 'X':
                if letter in word:
                    valid = False
                    break
            elif feedback[i] == 'G':
                if word[i] != letter:
                    valid = False
                    break
            elif feedback[i] == 'Y':
                if letter not in word or word[i] == letter:
                    valid = False
                    break

        if valid:
            filtered_words[word] = word_bank[word]

    return filtered_words

def select_guess_by_entropy(word_bank):
    if not word_bank:
        return None  
    return max(word_bank.keys(), key=lambda w: word_bank[w])

def play_wordle(word_bank):
    guesses = 5
    guess_1 = "slate"
    print(f"Guess 1: {guess_1}")
    
    fb = input("Enter feedback for guess 1 (G/Y/X): ").strip().upper()
    word_bank = remove_non_words(word_bank, guess_1, fb)
    print(f"Remaining words: {len(word_bank)}")

    while guesses > 0 and len(word_bank) > 0:
        guess = select_guess_by_entropy(word_bank)
        print(f"Guess {6 - guesses}: {guess}")
        
        fb = input(f"Enter feedback for guess {6 - guesses} (G/Y/X): ").strip().upper()
        word_bank = remove_non_words(word_bank, guess, fb)
        if fb == "GGGGG":
            print("You win!")
            return
        guesses -= 1
        print(f"Remaining words: {len(word_bank)}")

    print("Game Over!")

word_bank = read_word_bank("word-bank.csv")
play_wordle(word_bank)