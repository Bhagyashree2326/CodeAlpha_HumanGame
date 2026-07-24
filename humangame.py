import random

# User enters 4 words
words = []

print("Enter 4 words:")
for i in range(4):
    word = input(f"Enter word {i+1}: ").lower()
    words.append(word)

# Randomly select one word
secret_word = random.choice(words)

# Create blanks
display = ["_"] * len(secret_word)

guessed_letters = []
wrong = 0
max_wrong = 3

print("\n===== HANGMAN GAME =====")

while "_" in display and wrong < max_wrong:

    print("\nWord:", " ".join(display))
    print("Wrong guesses left:", max_wrong - wrong)
    print("Guessed letters:", guessed_letters)

    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed this letter.")
    else:
        guessed_letters.append(guess)
        
        if guess in secret_word:
            print("Correct!")

            for i in range(len(secret_word)):
                if secret_word[i] == guess:
                    display[i] = guess
        else:
            print("Wrong!")
            wrong += 1
# Result
if "_" not in display:
    print("\n🎉 Congratulations! You guessed the word:", secret_word)
else:
    print("\n❌ Game Over!")
    print("The correct word was:", secret_word)