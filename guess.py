import random
randNum  = random.randint(1, 40)
print("Enter A number between 1 and 40")
guessNum = int(input("")

while guessNum  = randNum:
    if guessNum < randNum:
    print("Your Input Is Less Than The Number")
    guessNum = int(input("ENTER NEW NUMBER HERE... ")
    
    if guessNum > randNum:
    print("Your Input Is Higher Than The Number")
    guessNum = int(input("ENTER NEW NUMBER HERE... ")
    
    if guessNum == randNum:
    print("Your Input Is Correct")