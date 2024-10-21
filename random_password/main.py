# Generate Random Password

import random
import string


def generatePassword(length):
    characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for i in range(length))
    return password
    
length = 12

print(f"The generated password is {generatePassword(length)}")





