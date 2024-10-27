import random

data = ["programming", "developer", "computer", "coder"]
dashed = ""
randomData = random.choice(data)
print(randomData)

dashed = len(randomData)*("-")
dashed = list(dashed)
chance = 5

while chance > 0:
    for i in dashed:
        print(i, end="")
    print()
    guessLetter = input("Guess the letter: ").lower()
    if guessLetter in randomData:
        for i in range(len(randomData)):
            if guessLetter == randomData[i]:
                dashed[i] = guessLetter
        print("You got that right!")
        if "".join(dashed) == randomData:
            print("You Won!!!")
            break
    else:
        chance -= 1
        print("Nope, that's incorrect")
        print(f"You left with {chance} chance")
    
    
else:
    print("You Lost your all chance!!.")
    