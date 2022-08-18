import random
import re


def main():
    secretWord = random.choice(
        ["apple", "Japan", "curious", "onepiece", "fortune"])

    letterGuessed = ""

    failureCount = len(secretWord)

    print(f"Welcome to the hangman! You have {failureCount} chances to guess!")

    while failureCount > 0:
        guess = input("Enter a letter: ")
        # to check the input is valid or not
        while not (re.search("[a-zA-Z]", guess)) or not (len(guess) == 1):
            print("Incorrect input! Please input one character from a to z.")
            guess = input("Enter a letter: ")

        else:
            while guess in letterGuessed:
                print("You guessed this letter already. Please try another one")
                guess = input("Enter a letter: ")

            else:
                if guess in secretWord:
                    print(
                        f"Correct! There is one or more {guess} in the secret word.")

                else:
                    failureCount -= 1
                    print(
                        f"incorrect. There is no {guess} in the secret word. {failureCount} turn(s) left.")

                letterGuessed = letterGuessed + guess
                wrongLetterCount = 0

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
        print(f"Sorry! You lose!")


if __name__ == "__main__":
    main()
