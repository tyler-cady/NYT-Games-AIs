import random
from collections import defaultdict
from wordlebot2 import read_word_bank, remove_non_words, select_guess_by_entropy

def test_bot(word_bank):
    words = list(word_bank.keys())
    wins = 0
    total_guesses = []

    for solution in words:
        word_bank_copy = word_bank.copy()
        guesses = 6  # Standard Wordle rules
        guess = "tares"  
        previous_guesses = set()

        while guesses > 0:
            previous_guesses.add(guess)
            feedback = get_feedback(guess, solution)  # Simulate Wordle feedback
            
            if feedback == "GGGGG":  # Bot wins
                wins += 1
                total_guesses.append(6 - guesses + 1)
                break
            
            word_bank_copy = remove_non_words(word_bank_copy, guess, feedback)
            if not word_bank_copy:  # No words left to guess
                break
            
            guess = select_guess_by_entropy(word_bank_copy)
            while guess in previous_guesses and len(word_bank_copy) > 1:
                guess = select_guess_by_entropy(word_bank_copy)
            
            guesses -= 1

        else:
            total_guesses.append(6)  # Max guesses used

    avg_guesses = sum(total_guesses) / len(total_guesses)
    win_rate = wins / len(words) * 100

    print(f"Bot played {len(words)} games.")
    print(f"Win rate: {win_rate:.2f}%")
    print(f"Average guesses per win: {avg_guesses:.2f}")

# Helper function to simulate Wordle feedback
def get_feedback(guess, solution):
    feedback = []
    for i, letter in enumerate(guess):
        if letter == solution[i]:
            feedback.append("G")  # Green (correct position)
        elif letter in solution:
            feedback.append("Y")  # Yellow (wrong position)
        else:
            feedback.append("X")  # Gray (not in word)
    return "".join(feedback)


test_bot(read_word_bank("word-bank.csv"))
