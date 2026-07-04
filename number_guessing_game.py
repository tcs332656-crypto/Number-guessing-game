import random

print("Welcome to the number guessing game")
#this is to welcome the user
Guess = int(input("Guess a number from the range 1 to 100 : "))
#this will take users input
TheSecret_Number = random.randint(1, 100)
#this will help the computer choose a random number
count = 1
#this tracks the number of guesses
while Guess  != TheSecret_Number :
    #the loop works until the user guesses the correct number
    if Guess  > TheSecret_Number  :
        #this is to check if users guess is more than the number decided by the computer
        print("Sorry your guess in incorrect , try a lower number")
        #this tells user that their gues is wrong
    elif Guess  < TheSecret_Number  :
        #this is to check if users guess is less than the number decided by the computer
        print("Sorry your guess in incorrect , try a higher number")
        #this tells user that their gues is wrong

    Guess  = int(input("Guess again : "))
    #this tells the user to guess again
    count += 1
    #this tracks the number of guesses

print(f"Congratulations ! You guessed it after {count} tries")
#this tells the user that they guessed the right number
