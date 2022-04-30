#Step 5

import random
import hangman_art
import hangman_words
from replit import clear

#Update the word list to use the 'word_list' from hangman_words.py
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
logo = hangman_art.logo


end_of_game = False
lives = 6

#Import the logo from hangman_art.py and print it at the start of the game.

print(logo)
#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"
print(f"{' '.join(display)}")
print(hangman_art.stages[6])

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    clear()
    
    #If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
      print(f"You've already guessed the letter {guess}")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        #If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"Sorry, the letter {guess} is not in the word, you lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # Import the stages from hangman_art.py and make this error go away.
    print(hangman_art.stages[lives])