import random

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
            'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
            'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
specialCharacters = ['!', '"', '#', '$', '%', '&', "'", '(', ')',
                     '*', '+', ',', '-', '.', '/', ':', ';',
                     '<', '=', '>', '?', '@', '[', '\\', ']',
                     '^', '_', '`', '{', '|', '}', '~']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# input to generate random password
getRandomAlphabets = int(input('How many letters would you like?\n'))
getRandomSpecialChar = int(input('How many symbols would you like?\n'))
getRandomNumbers = int(input('How many numbers would you like?\n'))

# generate components of the password
passwordList = []

for char in range(1, getRandomAlphabets + 1):
    passwordList.append(random.choice(alphabet))

for char in range(1, getRandomNumbers + 1):
    passwordList.append(random.choice(numbers))

for char in range(1, getRandomSpecialChar + 1):
    passwordList.append(random.choice(specialCharacters))

# shuffle the generated password
random.shuffle(passwordList)

# join the elements of the list
# password = ''.join(passwordList)

for char in passwordList:
    passwordList += char

print(passwordList)