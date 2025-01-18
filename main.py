import pandas as pd
import nltk
from nltk.corpus import words

nltk.download('words')

# Get the list of valid words
word_list = words.words()

# Filter 5-letter words
valid_5_letter_words = [word for word in word_list if len(word) == 5]

# Function for complex search conditions with exclusion, no repeated letters, and specific letter positions
def search_words(must_contain=None, must_not_contain=None, must_start_with=None, must_end_with=None, no_repeats=False, specific_positions=None):
    results = valid_5_letter_words
    
    if must_contain:
        must_contain = [c.upper() for c in must_contain]
        results = [word for word in results if all(c in word.upper() for c in must_contain)]
    
    if must_not_contain:
        must_not_contain = [c.upper() for c in must_not_contain]
        results = [word for word in results if all(c not in word.upper() for c in must_not_contain)]
    
    if must_start_with:
        results = [word for word in results if word.upper().startswith(must_start_with.upper())]
    
    if must_end_with:
        results = [word for word in results if word.upper().endswith(must_end_with.upper())]
    
    # if no_repeats:
    #     results = [word for word in results if len(set(word)) == len(word)]
    
    if specific_positions:
        for pos, letter in specific_positions.items():
            results = [word for word in results if word.upper()[pos] == letter.upper()]
    
    if results:
        print(f"Words matching the criteria:")
    
        for word in results:
            print(f"{word}")
    else:
        print("No words match the criteria.")

# Interactive search interface
def interactive_search():
    while True:
        print("\nSelect a search option:")
        print("1. Search for words with conditions")
        print("2. Exit")
        choice = input("Enter your choice (1-2): ")
        if choice == '1':
            must_contain = input("Enter letters that must be contained (comma-separated, e.g., 'S,A'): ").split(',')
            must_not_contain = input("Enter letters that must not be contained (comma-separated, e.g., 'R,T'): ").split(',')
            must_start_with = input("Enter the prefix that the words must start with (leave blank if none): ")
            must_end_with = input("Enter the suffix that the words must end with (leave blank if none): ")
            no_repeats = 'no'
            specific_positions = {}
            while True:
                pos_input = input("Enter a specific position and letter (format: position,letter; e.g., '0,P' for P at the first position), or press Enter to finish: ")
                if pos_input:
                    try:
                        pos, letter = pos_input.split(',')
                        pos = int(pos)
                        if 0 <= pos < 5:
                            specific_positions[pos] = letter.strip().upper()
                        else:
                            print("Position must be between 0 and 4.")
                    except ValueError:
                        print("Invalid format. Please use the format: position,letter")
                else:
                    break
            must_contain = [c.strip() for c in must_contain if c.strip()]
            must_not_contain = [c.strip() for c in must_not_contain if c.strip()]
            search_words(
                must_contain=must_contain, 
                must_not_contain=must_not_contain, 
                must_start_with=must_start_with, 
                must_end_with=must_end_with,
                no_repeats=no_repeats,
                specific_positions=specific_positions
            )
        elif choice == '2':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 2.")

# Run the interactive search interface
interactive_search()
