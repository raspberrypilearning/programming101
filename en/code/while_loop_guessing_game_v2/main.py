playing = True
number = 89
guesses = 0

while playing == True:
    guess = input("Guess a number between 1 and 100 > ")
    guess_int = int(guess)

    if guess == number:
        print("You got it right!")
        playing = False
    else:
        print("Try again!")
        guesses = guesses + 1

    if guesses > 3:
        print("You have run out of guesses, goodbye")
        playing = False
