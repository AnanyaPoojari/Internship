import random

def guess_number():
    number = random.randint(1, 100)
    attempts = 0
    guessed = False

    print("Guess the number between 1 and 100!")

    while not guessed:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess == number:
                print(f"Congratulations! You've guessed the number {number} in {attempts} attempts!")
                guessed = True
            elif guess < number:
                print("Too low! Try a higher number.")
            else:
                print("Too high! Try a lower number.")
        except ValueError:
            print("Please enter a valid number.")

def play_game():
    play_again = True

    while play_again:
        guess_number()
        play = input("Do you want to play again? (yes/no): ").lower()
        if play != "yes":
            play_again = False
            print("Thanks for playing!")

play_game()