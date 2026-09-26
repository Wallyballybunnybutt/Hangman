import random

def hangman():
    words = ['banana', 'minion', 'rabbit', 'donut', 'dance']
    wrongGuess = 6
    print("Welcome to hangman!")
    word = random.choice(words)
    guessed = []
    winner = False

    while wrongGuess > 0:
        display = ""
        guess = input("What letter would you like to guess?")
        if guess in guessed:
            print("You've already guessed that!")
            continue
        
        if guess in word:
            print("Correct!")
            guessed.append(guess)
        else:
            wrongGuess -= 1
            print("Wrong! you have ", wrongGuess," left")
        for letter in word:
            if letter in guessed:
                display += letter
            else:
                display += "_"
        print(display)

        if display == word:
            winner = True
            break

    if winner:
        print("You have won hangman!")
        print("The word was: ", word)
    else:
        print("Gamover! The word was: ", word)
hangman()
