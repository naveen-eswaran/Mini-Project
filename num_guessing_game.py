import random

print("🎯 Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100...")

secret_number = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("\nEnter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("📈 Too Low! Try higher.")
    elif guess > secret_number:
        print("📉 Too High! Try lower.")
    else:
        print(f"🎉 Correct! You got it in {attempts} attempts!")
        break