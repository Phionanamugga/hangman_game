#Creates the hangman game
import random
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(f'Psst, the solution is {chosen_word}.')
display = []
for letter in chosen_word:
    display += "_"
    print(display)


guess = input("Guess a letter:").lower()
for position in range(len(chosen_word)):
    if letter == guess:
        print("Right")
    else:
        print("Wrong")
