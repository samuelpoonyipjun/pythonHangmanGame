import random
from hangman_words import new_word_list
chosen_word = random.choice(new_word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 9
from hangman_art import logo
print(logo)
display = []
guessed_letters = []
for i in range(word_length):
    display.append("_")
while not end_of_game:
    print(f"{' '.join(display)}")
    guess = input("Guess a letter: ").lower()
    if guess in guessed_letters:
        print(f"You've already guessed {guess}")
        if guess not in chosen_word:
            print("It is not in the word. Try something else, dont give up.")
    else:
        guessed_letters.append(guess)
        if guess not in chosen_word:
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
            lives -= 1
            if lives == 0:
                end_of_game = True
                print(f"You lose. The word was {chosen_word}")
        else:
            for position in range(word_length):
                letter = chosen_word[position]
                if letter == guess:
                    display[position] = letter
    if "_" not in display:
        end_of_game = True
        print("You win.")
        print(logo)
        print(f"{' '.join(display)}")
    from hangman_art import stages
    print(stages[lives])