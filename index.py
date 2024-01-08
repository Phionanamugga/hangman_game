#Creates the hangman game
import random
word_list = ["abruptly", "absurd", "abyss", "affix", "axion","azure", "bagpipes"
             "ardvark", "baboon", "camel", "bikini", "bayou", "blizzard", "beekeeper"]
chosen_word = random.choice(word_list)
print(f'Psst, the solution is {chosen_word}.')
display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"
    print(display)

end_of_game = False
while not end_of_game:
    guess = input("Guess a letter:").lower()
    for position in range(word_length):
        letter = chosen_word[position]
        print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
    print(display)

    if "_" not in display:
        end_of_game = True
        print("You win")

    lives = 6
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose")