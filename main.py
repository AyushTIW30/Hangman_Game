import random
from Hangman_art import logo, stages
from Hangman_hg import word_list

# -----------------------------
# 🎮 Welcome Message
# -----------------------------
print(logo)
print("Welcome to Hangman!\n")

# -----------------------------
# 🎯 Choose a Random Word
# -----------------------------
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = len(stages) - 1  # Total stages available
end_of_game = False

# For testing: Uncomment the next line to see the word
# print(f"[DEBUG] The word is: {chosen_word}")

# -----------------------------
# 🧩 Game Setup
# -----------------------------
display = ["_"] * word_length
guessed_letters = []

# -----------------------------
# 🔁 Game Loop
# -----------------------------
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # ✅ Validate input
    if not guess.isalpha() or len(guess) != 1:
        print("⚠️ Please enter a single alphabet letter.")
        continue

    if guess in guessed_letters:
        print(f"🔁 You've already guessed '{guess}'. Try a different letter.")
        continue

    guessed_letters.append(guess)

    # 🔍 Check guessed letter
    if guess in chosen_word:
        for position in range(word_length):
            if chosen_word[position] == guess:
                display[position] = guess
        print(f"✅ Good guess!")
    else:
        lives -= 1
        print(f"❌ '{guess}' is not in the word. You lost a life.")
        if lives == 0:
            end_of_game = True
            print("\n💀 You lose!")
            print(f"The word was: {chosen_word}")

    # 📄 Display current progress
    print("\nWord:", " ".join(display))
    print(stages[lives])
    print(f"Lives left: {lives}")
    print(f"Guessed so far: {', '.join(guessed_letters)}\n")

    # 🏁 Win Condition
    if "_" not in display:
        end_of_game = True
        print("🎉 You win! Great job guessing the word!")

