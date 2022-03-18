secret_word = "elephant"
guess_word = ""
times_guess = 0
guess_limit = 3
out_of_guesses = False

# loop until you guess the correct word or until you are out of tries
while guess_word != secret_word and not(out_of_guesses):
    if times_guess < guess_limit:
        guess_word = input("Enter your guess : ")
        times_guess += 1
    else:
        out_of_guesses = True 

if out_of_guesses:
    print("Out of guesses, you lost.")
else:    
    print("You found it, you won!")    