# Init var
from random_word import RandomWords
from hangman_art import logo
from hangman_art import stages

print(logo)
r = RandomWords()
word_to_guess = r.get_random_word()
while word_to_guess is None:
    word_to_guess = r.get_random_word()
print(f"The correct word is {word_to_guess} with len {len(word_to_guess)}")
number_of_lives = len(stages)
end_game = False
blank_word = ["_" for x in range(len(word_to_guess))]
while not end_game:
    guess = input(f"Guess a letter : \n").lower()
    for position in range(len(word_to_guess)):
        letter = word_to_guess[position]
        if guess == letter:
            blank_word[position] = guess
    if guess not in word_to_guess:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        number_of_lives -= 1
        print(stages[number_of_lives])
        if number_of_lives == 0:
            end_game = True
            print("You lose !!!!!")
    else:
        print(f"You've already guessed {guess}")
    print(f"{' '.join(blank_word)}")
    if "_" not in blank_word:
        end_game = True
        print("You win!!!!!")
