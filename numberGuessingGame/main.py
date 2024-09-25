import random

random_number = random.randint(1,100)
total_attempts = 3

attempt = 0
while attempt < 3:
    guess = int(input("Guess a number between 1 and 100: "))
    
    if guess > random_number:
        print("Too high")
        attempt += 1
    elif guess < random_number:
        print("Too low")
        attempt += 1
    elif guess == random_number:
        print("You Won!!! ✅")
        break
else:
    print("You Lost!! ❌")
    print(f"Generated number is {random_number}")