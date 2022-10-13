import random
import re


def main():
    playAgain = "y"
    # loop is used so the player can choose to play another time or not after one game
    while playAgain == "y":
        secretWord = random.choice(
            ["apple", "japan", "curious", "onepiece", "fortune"])

        letterGuessed = ""
        
        failureCount = len(secretWord)

        print(f"Welcome to the hangman! You have {failureCount} chances to fail!")

        while failureCount > 0:
            guess = (input("Enter a letter: ").lower())
            # to check if the input is valid or not
            while not (re.search("[a-zA-Z]", guess)) or not (len(guess) == 1):
                print("Incorrect input! Please input one character from a to z.")
                guess = input("Enter a letter: ").lower()

            else:
                # to check if the letter has been guessed before or not
                while guess in letterGuessed:
                    print("You guessed this letter already. Please try another one")
                    guess = input("Enter a letter: ").lower()

                else:
                    #to check if the guessed letter is in the secret word or not
                    if guess in secretWord:
                        print(
                            f"Correct! There is one or more {guess} in the secret word.")

                    else:
                        failureCount -= 1
                        print(
                            f"incorrect. There is no {guess} in the secret word. {failureCount} turn(s) left.")

                    letterGuessed = letterGuessed + guess
                    wrongLetterCount = 0

                    #to print out the current status of the secret word with correctly guessed letter(s)
                    for letter in secretWord:
                        if letter in letterGuessed:
                            print(f"{letter}", end="")
                        else:
                            print(f"_", end="")
                            wrongLetterCount += 1
                    print("\n")

                    if wrongLetterCount == 0:
                        print(
                            f"Congratulations! The secret word was :{secretWord}. You won!")
                        break
        else:
            print("Sorry! You lose!")
        playAgain = input("Do you want to play again? Y/N\n").lower()
        while (playAgain not in ("y","n")):
            print("Invalid input! Please enter Y for continuing the game and N for exit.")
            playAgain = input("Do you want to play again? Y/N\n").lower()
        if playAgain == "y":
            playAgain == "y"
        elif playAgain == "n":
            break

   


if __name__ == "__main__":
    main()
