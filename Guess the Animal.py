

print("Welcome to Guess the Animal!")
print("I'm thinking of an animal, can you guess what it is?")

# The animal the user needs to guess
secret_animal = "elephant"

# Hint to be displayed if user makes an incorrect guess
hint = "It has a long trunk and big ears"

# Loop until the user guesses the correct animal
while True:
    guess = input("Enter your guess: ")

    if guess.lower() == secret_animal:
        print("Congratulations, you guessed it!")
        break
    else:
        print("Sorry, that's not it. Here's a hint: " + hint)






