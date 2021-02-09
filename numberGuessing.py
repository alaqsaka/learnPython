# importing random library 

import random 

def inputNumber(message):
    while True: 
        try: 
            number = int(input(message))
        except ValueError:
            print("Please enter a number not a string/text ")
            continue
        else: 
            return number 
            
def guess(number):
    i = 0
    numberToGuess: int = random.randint(1, number)
    print(numberToGuess)
    while(i<=3):
        userGuess = int(input("What's the number? "))
        if (numberToGuess == userGuess):
            print("You Win :D")
            break
        else: 
            print("Wrong number. Please try again.")
            i+=1
            if (i == 2):
                print("You Lose. Please try again next time ^^ ")
                break
    
# Main code
print("Welcome to random guessing game.")
name = input("Enter your name: ")

print("Rules: \n1. User choose the range of numbers \n2. User have three times for guess")

print("\nLet's get started. ")

number = inputNumber("Enter the maximum number ")

print(f"The range is from 1 to {number}")

guess(number)

print("Thanks for playing :D")
