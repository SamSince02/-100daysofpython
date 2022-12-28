import random 
import art

print(art.logo2)

print("Welcome to the number guessing game !\n")

def guess_number():
    global number
    number = random.randint(1,100) 
    print("I'm thinking of a number between 1 and 100\n")
    return number

guess_number()

diffi_lvl = input("Choose a difficulty level.Type 'easy' or 'hard' : \n")

if diffi_lvl == "easy":
    attempts = 10
    while attempts !=0:
        print(f"You have {attempts} attempts remaining to guess the number.\n")
        guess = int(input("Make a guess : "))
        if guess > number:
            print("\nToo High.\nGuess again.\n")
        elif guess < number:
            print("\nToo low.\nGuess again.\n")
        elif guess ==number:
            print(f"You got it ! The answer was {number}")
            break
        attempts = attempts - 1
elif diffi_lvl == "hard":
    attempts = 5
    while attempts !=0:
        print(f"You have {attempts} attempts remaining to guess the number.\n")
        guess = int(input("Make a guess : "))
        if guess > number:
            print("\nToo High.\nGuess again.\n")
        elif guess < number:
            print("\nToo low.\nGuess again.\n")
        elif guess ==number:
            print(f"You got it ! The answer was {number}")
            break
        attempts = attempts - 1
else:
    print("Enter the valid inputs")

