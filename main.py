import random  # Step 1: Import the random library to generate a secret number

def guess_the_number():
    # Step 2: Set the game boundaries and pick the secret number
    secret_number = random.randint(1, 100)
    attempts = 0
    
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")

    # Step 3: Start a loop so the player can keep guessing
    while True:
        try:
            # Step 4: Get input from the user and convert it to an integer
            user_guess = int(input("Take a guess: "))
            attempts += 1  # Track how many turns you take
            
            # Step 5: Use conditional logic to check the guess
            if user_guess < secret_number:
                print("Too low! Try again.")
            elif user_guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"🎉 Correct! You found the number in {attempts} attempts!")
                break  # Stop the loop since the player won
                
        except ValueError:
            print("Please enter a valid round number.")

# Run the game
guess_the_number()
