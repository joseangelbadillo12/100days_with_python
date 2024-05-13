import random
import hangman_words
from hangman_art import logo,stages

lives = 6
random_word = random.choice(hangman_words.word_list)
won = False
blank_list = []
for letters in range(0, len(random_word)):
    blank_list.append("_")

print(logo)

while not won:
    guess = input("Guess a letter: ").lower()
    if guess in blank_list:
      print(f"You've already guessed {guess}")
    for guessed in range(0, len(random_word)):
        if guess == random_word[guessed]:
            blank_list[guessed] = guess
            print(f"{' '.join(blank_list)}")
    if guess not in random_word:
        print(stages[lives])
        lives -= 1
        print(f"{' '.join(blank_list)}")
    if lives == 0:
        print("You lose!")
        print(f"The word was {random_word}")
        break
    if "_" not in blank_list:
        won = True
        print("You won!")

